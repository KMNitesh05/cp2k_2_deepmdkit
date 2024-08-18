import numpy as np

def convert_forces_and_energy_to_raw(file_path, natoms, force_output_file, energy_output_file, start_snapshot, end_snapshot):
    """
    Convert a file with atomic force data and energy values to formatted .raw files,
    including only snapshots within a specified range and converting forces to eV/Å
    and energy to eV.

    Parameters:
    file_path (str): Path to the input file.
    natoms (int): Number of atoms per frame.
    force_output_file (str): Path to the output .raw file for forces.
    energy_output_file (str): Path to the output .raw file for energy.
    start_snapshot (int): The starting snapshot number to include in the output files.
    end_snapshot (int): The ending snapshot number to include in the output files.
    """
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Conversion factors
    force_conversion_factor = 51.42208618  # Hartree/Bohr to eV/Å
    energy_conversion_factor = 27.2114079527  # Hartree to eV

    forces = []
    energies = []
    current_frame = []
    frame_line_counter = 0
    snapshot_counter = 0

    for line in lines:
        frame_line_counter += 1

        if frame_line_counter == 2:
            # Extract and convert the energy value
            energy = float(line.split('=')[-1].strip()) * energy_conversion_factor

        # Skip the first two lines of each frame (header and additional information)
        if frame_line_counter <= 2:
            continue

        # Extract the force components and convert them to eV/Å
        parts = line.split()
        if len(parts) == 4:  # Format: atom_type fx fy fz
            force = [float(parts[1]) * force_conversion_factor, 
                     float(parts[2]) * force_conversion_factor, 
                     float(parts[3]) * force_conversion_factor]
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
            energies.append(energy)
            current_frame = []
            frame_line_counter = 0  # Reset for next frame

    # Save the forces array to the output file in the required format
    with open(force_output_file, 'w') as f:
        for frame in forces:
            # Write the entire frame (all atoms' forces) on one line with tab spacing
            f.write('\t'.join(f'{component:.6f}' for component in frame) + '\n')

    # Save the energies array to the output file in the required format
    with open(energy_output_file, 'w') as f:
        for energy in energies:
            f.write(f'{energy:.6f}\n')

def main():
    file_path = input("Enter the path to the input file: ")
    natoms = int(input("Enter the number of atoms per frame: "))
    start_snapshot = int(input("Enter the starting snapshot number: "))
    end_snapshot = int(input("Enter the ending snapshot number: "))
    
    force_output_file = 'force.raw'  # Path to the output .raw file for forces
    energy_output_file = 'energy.raw'  # Path to the output .raw file for energy
    
    convert_forces_and_energy_to_raw(file_path, natoms, force_output_file, energy_output_file, start_snapshot, end_snapshot)
    print(f"Files successfully saved to {force_output_file} and {energy_output_file}")

if __name__ == '__main__':
    main()
