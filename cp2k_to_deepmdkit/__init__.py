import numpy as np

def convert_forces_to_raw_formatted(file_path, natoms, output_file, start_snapshot, end_snapshot):
    """
    Convert a file with atomic force data to a formatted .raw file with a new line for each frame,
    including only snapshots within a specified range.

    Parameters:
    file_path (str): Path to the input file.
    natoms (int): Number of atoms per frame.
    output_file (str): Path to the output .raw file.
    start_snapshot (int): The starting snapshot number to include in the output file.
    end_snapshot (int): The ending snapshot number to include in the output file.
    """
    with open(file_path, 'r') as file:
        lines = file.readlines()

    forces = []
    current_frame = []
    frame_line_counter = 0
    snapshot_counter = 0

    for line in lines:
        frame_line_counter += 1

        # Skip the first two lines of each frame (header and additional information)
        if frame_line_counter <= 2:
            continue

        # Extract the force components
        parts = line.split()
        if len(parts) == 4:  # Format: atom_type fx fy fz
            force = [float(parts[1]), float(parts[2]), float(parts[3])]  # Extracting fx, fy, fz
            current_frame += force  # Append force components directly to current_frame

        # Check if we reached the end of the frame
        if frame_line_counter == natoms + 2:
            snapshot_counter += 1
            if snapshot_counter < start_snapshot:
                current_frame = []
                frame_line_counter = 0
                continue
            elif snapshot_counter > end_snapshot:
                break

            forces.append(current_frame)
            current_frame = []
            frame_line_counter = 0  # Reset for next frame

    # Save the forces array to the output file in the required format
    with open(output_file, 'w') as f:
        for frame in forces:
            # Write the entire frame (all atoms' forces) on one line with tab spacing
            f.write('\t'.join(f'{component:.6f}' for component in frame) + '\n')

if __name__ == "__main__":
    file_path = input("Enter the path to the input file: ")
    natoms = int(input("Enter the number of atoms per frame: "))
    start_snapshot = int(input("Enter the starting snapshot number: "))
    end_snapshot = int(input("Enter the ending snapshot number: "))
    output_file = 'coord.raw'  # Path to the output .raw file
    
    convert_forces_to_raw_formatted(file_path, natoms, output_file, start_snapshot, end_snapshot)
    print(f"File successfully saved to {output_file}")
