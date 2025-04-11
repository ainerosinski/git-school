import os
import shutil

def move_file(source_path, destination_path):
    if not os.path.exists(destination_path):
        os.makedirs(destination_path)
    
    # Move file
    with open(source_path, 'rb') as f:
        shutil.move(f, destination_path)

# Example usage
move_file("/path/to/source/file", "/path/to/destination")
