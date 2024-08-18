import numpy as np

def convert_raw_to_npy(raw_file_path):
    """
    Convert a raw file to a numpy file (.npy) with the same filename.

    Parameters:
    raw_file_path (str): Path to the raw file.
    """
    # Read the raw file data
    data = np.loadtxt(raw_file_path)

    # Determine the .npy file path
    npy_file_path = raw_file_path.rsplit('.', 1)[0] + '.npy'

    # Save the data as a numpy file
    np.save(npy_file_path, data)

    return npy_file_path

def main():
    raw_file_path = input("Enter the path to the raw file: ")
    npy_file_path = convert_raw_to_npy(raw_file_path)
    print(f"File successfully converted to {npy_file_path}")

if __name__ == '__main__':
    main()
