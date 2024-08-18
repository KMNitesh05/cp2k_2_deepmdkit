# cp2k_2_deepmdkit (c2d)

## CP2K Output to DEEPMD-KIT Input Generator

This python package provides command-line tools to convert CP2K output files into DEEPMD-KIT input formats. The tools are prefixed with `c2d-` for tasks such as converting coordinates, forces, energies, and box dimensions.

## Installation

Clone the repository and install the package with `pip`:

```bash
git clone https://github.com/KMNitesh05/cp2k_2_deepmdkit.git 
cd cp2k_2_deepmdkit
pip install .
```

Usage
1. Generate box.raw file:
Run c2d-box and input values as prompted:

```bash
c2d-box
Enter the number of rows: 5
Enter the value for X: 19.00
Enter the value for Y: 19.00
Enter the value for Z: 19.00
```

2. Generate coord.raw file:
Run c2d-coord to convert coordinates:

```bash
c2d-coord
Enter the path to the input file: test.xyz
Enter the number of atoms per frame: 5
Enter the starting snapshot number: 0
Enter the ending snapshot number: 5
```

3. Generate force.raw and energy.raw files:
Run c2d-force_energy to convert forces and energies:

```bash
c2d-force_energy
Enter the path to the input file: test.for
Enter the number of atoms per frame: 120
Enter the starting snapshot number: 0
Enter the ending snapshot number: 5
```

4. Convert raw files to .npy format:
Run c2d-convert to convert .raw files to .npy:

```bash
c2d-convert
Enter the path to the raw file: box.raw
```

Examples: 
Test the commands using example files in the examples directory:

```bash
c2d-box examples/box.xyz
c2d-coord examples/coord.xyz
c2d-force_energy examples/force_energy.raw
c2d-convert examples/box.raw
```

Contact:
Nitesh Kumar
Email: niteshgoesactive@gmail.com

Citation:
Please cite this package if you find it useful in your research:

```bash
@misc{c2d,
  title={c2d: A Python Package to convert CP2K output to DEEPMD-KIT input},
  author={Nitesh Kumar},
  year={2024},
  howpublished={\url{https://github.com/KMNitesh05/cp2k_2_deepmdkit}},
  note={Washington State University, Pullman, WA, United States 99163}
}
```

