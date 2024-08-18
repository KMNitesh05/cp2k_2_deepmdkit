# cp2k_2_deepmdkit

## CP2K Putput to DEEPMD-KIT Input Converter

This package allows for the conversion of CP2K output files to DEEPMD-KIT input files with ease. It includes several command-line tools prefixed with `c2d-` for different tasks.

## Installation

To install the package, clone the repository and use `pip`:

```bash
git clone https://github.com/yourusername/CP2K_to_DEEPMDKIT.git
cd CP2K_to_DEEPMDKIT
pip install .


## Usage

1. **Generate `box.raw` file**:
   Run the command `c2d-box` and input the values as prompted. This will create a `box.raw` file with the specified dimensions.

   ```sh
   c2d-box
   Enter the number of rows: 5
   Enter the value for X: 19.00
   Enter the value for Y: 19.00
   Enter the value for Z: 19.00

