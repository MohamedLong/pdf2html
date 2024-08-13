# Run this in a script or interactive Python session in the Docker container
import os

output_file_path = 'tmp/output.html'

if os.path.exists(output_file_path):
    with open(output_file_path, 'r') as f:
        print(f.read())
else:
    print("File not found")
