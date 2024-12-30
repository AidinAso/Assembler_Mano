# Assembler_Mano
This project implements an assembler based on Morris Mano's basic computer architecture, translating assembly code to machine code. It uses symbol table management and a two-pass process for label analysis and instruction conversion, aligning with the defined format and aiding in understanding digital systems.

# Assembler Implementation for Mano's Computer Architecture

## Description
This project is an implementation of the assembler for the Mano Computer Architecture, as described in the classic computer systems design book. The assembler performs two passes to process a simplified assembly language:
1. The first pass constructs a symbol table with addresses for all defined labels.  
2. The second pass generates machine code for instructions and data.

The output of the assembler includes:
- **Symbol Table**: Labels with their corresponding memory addresses in both hexadecimal and binary formats.
- **Machine Code**: Assembly instructions translated into their respective machine code, represented in both hexadecimal and binary formats.

## Features
- **Two-Pass Assembler**: Implements the `ORG`, `DEC`, `HEX`, and `END` pseudo-operations and instructions based on Mano's opcode table.
- **Flexible Input**: Users can modify the assembly code input as a Python list.
- **Error Handling**: Alerts if undefined symbols are used in the assembly code.
- **Formatted Output**: Displays symbol table and machine code in hexadecimal and binary formats.

## Technologies Used
- **Python**: The project is implemented in Python for simplicity and accessibility.

## How It Works
1. **First Pass**
   - The assembler reads each line of the assembly program.
   - If a label is found, it adds the label and its associated memory address to the symbol table.
   - For `ORG`, sets the initial value of the location counter (LC).
   - Ignores comments and processes the program until `END` is reached.

2. **Second Pass**
   - The assembler uses the symbol table to replace labels with their respective addresses.
   - Translates assembly instructions into machine code using the opcode table.
   - Handles data definitions (e.g., `DEC`, `HEX`).
   - Outputs the final machine code list.

## Sample Assembly Code
Here is an example input program:
```assembly
ORG 100
LDA NUM1
ADD NUM2
STA SUM
HLT
NUM1, DEC 45
NUM2, DEC 78
SUM, HEX 0
END
```

### Output
#### Symbol Table:
```
NUM1: Hex=104, Bin=0000000100000100
NUM2: Hex=105, Bin=0000000100000101
SUM:  Hex=106, Bin=0000000100000110
```

#### Machine Code:
```
Hex=2104, Bin=0010000100000100
Hex=1105, Bin=0001000100000101
Hex=3106, Bin=0011000100000110
Hex=7001, Bin=0111000000000001
Hex=002D, Bin=0000000000101101
Hex=004E, Bin=0000000001001110
Hex=0000, Bin=0000000000000000
```

## Usage
1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```
2. Modify the `assembly_code` list in the Python script to input your desired assembly program.
3. Run the script:
   ```bash
   python assembler.py
   ```
4. View the symbol table and machine code in the console output.

## Opcode Table
The assembler uses the following opcode mappings:
```python
opcode_table = {
    "AND": "0",
    "ADD": "1",
    "LDA": "2",
    "STA": "3",
    "BUN": "4",
    "BSA": "5",
    "ISZ": "6",
    "CLA": "7800",
    "CLE": "7400",
    "CMA": "7200",
    "CME": "7100",
    "CIR": "7080",
    "CIL": "7040",
    "INC": "7020",
    "SPA": "7010",
    "SNA": "7008",
    "SZA": "7004",
    "SZE": "7002",
    "HLT": "7001",
    "INP": "F800",
    "OUT": "F400",
    "SKI": "F200",
    "SKO": "F100",
    "ION": "F080",
    "IOF": "F040",
}
```

## Roadmap
- Add support for error logging and advanced validation.
- Implement macros for more complex assembly tasks.
- Support additional pseudo-operations.
- Create a web-based interface to upload and assemble code.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing
Contributions are welcome! Feel free to submit a pull request or open an issue.

## Acknowledgments
Special thanks to the authors of "Computer System Architecture" by M. Morris Mano for inspiring this project.

