import os
import subprocess
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/convert', methods=['POST'])
def convert_pdf_to_html():
    if 'file' not in request.files:
        return jsonify({"error": "No file provided"}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    if file:
        # Save the uploaded file
        input_file_path = '/tmp/input.pdf'
        output_file_path = 'tmp/output.html'
        file.save(input_file_path)

        # Convert PDF to HTML
        try:
            result = subprocess.run([
                'pdf2htmlEX', 
                input_file_path,
                output_file_path
            ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            if result.returncode != 0:
                stderr_output = result.stderr.decode('utf-8', errors='replace')
                return jsonify({"error": "Conversion failed", "stderr": stderr_output}), 500

            # Read the output HTML file
            with open(output_file_path, 'r', encoding='utf-8') as f:
                html_content = f.read()

            return html_content, 200

        except Exception as e:
            return jsonify({"error": str(e)}), 500

        finally:
            # Clean up files
            if os.path.exists(input_file_path):
                os.remove(input_file_path)
            if os.path.exists(output_file_path):
                os.remove(output_file_path)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
