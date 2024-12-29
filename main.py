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

symbol_table = {}

assembly_code = [
    "ORG 100",
    "LDA SUB",
    "CMA",
    "INC",
    "ADD MIN",
    "STA DIF",
    "HLT",
    "MIN, DEC 83",
    "SUB, DEC -23",
    "DIF, HEX 0",
    "END",
]

LC = 0

def first_pass():
    global LC
    for line in assembly_code:
        line = line.strip()
        if not line or line.startswith(";"):
            continue

        parts = line.split()
        label = None

        if "," in parts[0]:
            label, parts[0] = parts[0].replace(",", ""), parts[1]
            parts = parts[1:]

        if parts[0] == "ORG":
            LC = int(parts[1], 16)
        elif parts[0] == "END":
            break
        else:
            if label:
                symbol_table[label] = LC

            LC += 1

first_pass()

print("Symbol Table:", {k: f"{v:X}" for k, v in symbol_table.items()})
