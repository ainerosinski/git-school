import numpy as np

def load_and_process_data(file_path):
    data = np.loadtxt(file_path)
    # Add your processing logic here
    
if __name__ == "__main__":
    file_path = "path_to_your_file.txt"
    data = load_and_process_data(file_path)
    print(data)
