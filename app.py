from flask import Flask, request, jsonify
import os
import subprocess
import tempfile

app = Flask(__name__)

@app.route('/convert', methods=['POST'])
def convert_pdf_to_html():
    if not request.files:
        return jsonify({'error': 'No PDF file uploaded'}), 400

    pdf_files = request.files.getlist('pdf_files')  # Access multiple files

    if not pdf_files:
        return jsonify({'error': 'No PDF files uploaded'}), 400

    converted_html = []  # Store converted HTML for each PDF

    try:
        for pdf_file in pdf_files:
            # Extract filename without extension
            filename, _ = os.path.splitext(pdf_file.filename)

            with tempfile.NamedTemporaryFile(delete=False) as temp_pdf:
                pdf_file.save(temp_pdf.name)

                # Create unique output filename with extension
                output_filename = f'{filename}.html'  # Append .html extension

                command = ['pdf2htmlEX', temp_pdf.name, output_filename]  # Output to a file
                process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                output, error = process.communicate()

                if process.returncode != 0:
                    return jsonify({'error': f'PDF conversion failed: {error.decode()}'}), 500

                converted_html.append(output_filename)  # Store output filename

        return jsonify({'message': 'PDF conversion successful', 'html': converted_html}), 200
    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)
