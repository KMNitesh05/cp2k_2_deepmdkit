def create_and_save_box_file(new_values, num_rows, output_file):
    """
    Create a file with box dimensions based on specified values (X, Y, Z),
    extend it to a specified number of rows, and save to a new file.

    Parameters:
    new_values (tuple): The values to use for non-zero values (X, Y, Z).
    num_rows (int): The number of rows to create in the file.
    output_file (str): Path to the output file.
    """
    processed_lines = []

    # Creating each line with the specified X, Y, Z values
    line_template = "{} 0.000 0.000 0.000 {} 0.000 0.000 0.000 {}"
    line_content = line_template.format(*new_values)

    # Extend the file to the specified number of rows
    for _ in range(num_rows):
        processed_lines.append(line_content)

    # Save the lines to the output file
    with open(output_file, 'w') as file:
        for line in processed_lines:
            file.write(line + '\n')

def main():
    num_rows = int(input("Enter the number of rows: "))
    x_value = float(input("Enter the value for X: "))
    y_value = float(input("Enter the value for Y: "))
    z_value = float(input("Enter the value for Z: "))
    
    new_values = (x_value, y_value, z_value)
    output_file_path = 'box.raw'  # Path to the output file
    
    create_and_save_box_file(new_values, num_rows, output_file_path)
    print(f"File successfully saved to {output_file_path}")

if __name__ == '__main__':
    main()
