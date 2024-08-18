(* CP2K to DEEPMD-KIT Converter *)

(* Installation Instructions *)
(* Clone the repository and install the package using pip *)
"git clone https://github.com/yourusername/CP2K_to_DEEPMDKIT.git"
"cd CP2K_to_DEEPMDKIT"
"pip install ."

(* Usage Examples *)

(* Generate `box.raw` file *)
(* Run the command `c2d-box` and provide the required inputs *)
"c2d-box"
"Enter the number of rows: 5"
"Enter the value for X: 19.00"
"Enter the value for Y: 19.00"
"Enter the value for Z: 19.00"

(* Generate `coord.raw` file *)
(* Use `c2d-coord` to convert coordinate data to `.raw` format *)
"c2d-coord"
"Enter the path to the input file: test.xyz"
"Enter the number of atoms per frame: 5"
"Enter the starting snapshot number: 0"
"Enter the ending snapshot number: 5"

(* Generate `force.raw` and `energy.raw` files *)
(* Convert force and energy data using `c2d-force_energy` *)
"c2d-force_energy"
"Enter the path to the input file: test.for"
"Enter the number of atoms per frame: 120"
"Enter the starting snapshot number: 0"
"Enter the ending snapshot number: 5"

(* Convert raw files to `.npy` format *)
(* Use `c2d-convert` to convert raw files to numpy format *)
"c2d-convert"
"Enter the path to the raw file: box.raw"

(* Example Files *)
(* Test commands using example files in the `examples` directory *)
"c2d-box examples/box.xyz"
"c2d-coord examples/coord.xyz"
"c2d-force_energy examples/force_energy.raw"
"c2d-convert examples/box.raw"
