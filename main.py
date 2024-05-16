import subprocess

def convert_pdf_to_html(pdf_path, output_folder):
  command = ['pdf2htmlEX', pdf_path, output_folder]
  subprocess.run(command, check=True)
pdf_path = "BankMuscatReport.pdf"
output_folder = "output_html"
convert_pdf_to_html(pdf_path, output_folder)
