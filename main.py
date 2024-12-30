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

# Symbol Table
symbol_table = {}

# List of assembly code lines (for manual testing)
assembly_code = [
    "ORG 100",
    "LDA NUM1",
    "ADD NUM2",
    "STA SUM",
    "HLT",
    "NUM1, DEC 45",
    "NUM2, DEC 78",
    "SUM, HEX 0",
    "END",
]

# Initial value of LC
LC = 0

# First Pass
def first_pass():
    global LC
    for line in assembly_code:
        line = line.strip()
        if not line or line.startswith(";"):  # Ignore empty lines and comments
            continue

        parts = line.split()
        label = None

        if "," in parts[0]:  # If the line contains a label
            label, parts[0] = parts[0].replace(",", ""), parts[1]
            parts = parts[1:]

        if parts[0] == "ORG":
            LC = int(parts[1], 16)  # Set LC based on ORG
        elif parts[0] == "END":
            break
        else:
            if label:
                symbol_table[label] = LC  # Store label in symbol table

            LC += 1  # Increment LC after processing the line

# Second Pass
def second_pass():
    global LC
    LC = 0
    machine_code = []

    for line in assembly_code:
        line = line.strip()
        if not line or line.startswith(";"):  # Ignore empty lines and comments
            continue

        parts = line.split()
        if "," in parts[0]:  # If the line contains a label
            parts = parts[1:]

        if parts[0] == "ORG":
            LC = int(parts[1], 16)  # Set LC based on ORG
        elif parts[0] == "END":
            break
        elif parts[0] in opcode_table:  # Assemble instructions
            opcode = opcode_table[parts[0]]
            address = "0"

            if len(parts) > 1:  # Instruction with address
                if parts[1] in symbol_table:
                    address = f"{symbol_table[parts[1]]:03X}"
                else:
                    raise ValueError(f"Undefined symbol: {parts[1]}")

            if len(opcode) == 1:  # Standard instruction
                machine_code.append(f"{opcode}{address}")
            else:  # Special instruction
                machine_code.append(opcode)

            LC += 1
        elif parts[0] in ["DEC", "HEX"]:  # Data
            if parts[0] == "DEC":
                value = int(parts[1]) & 0xFFFF
            else:  # HEX
                value = int(parts[1], 16) & 0xFFFF

            machine_code.append(f"{value:04X}")
            LC += 1

    return machine_code

first_pass()
machine_code = second_pass()

# Print results in both hexadecimal and binary
print("Symbol Table:")
for symbol, address in symbol_table.items():
    print(f"{symbol}: Hex={address:X}, Bin={bin(address)[2:].zfill(16)}")

print("Machine Code:")
for code in machine_code:
    value = int(code, 16)
    print(f"Hex={code}, Bin={bin(value)[2:].zfill(16)}")
