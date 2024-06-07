from config import *
from number_manipulate import *
import re

def GenerateBinaryForR(line):
    """
    Generate the binary representation of an R-type MIPS instruction.

    Args:
        line (str): A single line string representing the R-type instruction
                    in the format "instruction Rd, Rs, Rt".

    Returns:
        str: A 32-bit binary string representing the machine code of the given R-type instruction.

    Example:
        line = "add $t1, $t2, $t3"
        result = GenerateBinaryForR(line)
        # result should be a 32-bit binary string.
    """
    # R-Type instruction
    # instruction Rd, Rs, Rt
    # index:    0, 1,  2,  3,

    # Machine code
    # Opcode Rs Rt Rd Shamt Func
    machine_code = ""
    shamt = "00000"         # 5-bit shamt

    tokens = line.split(" ")

    # INSTRUCTION_DECODED[key] = ['Type', 'Opcode', 'Func']
    type, opcode, func = INSTRUCTION_DECODED[tokens[0]]

    # Delete comma
    for idx, token in enumerate(tokens):
        if "," in token:
            tokens[idx] = tokens[idx].replace(",", "")

    instruction, rd, rs, rt = tokens

    # Append the opcode to the machine code string
    machine_code += opcode

    # Append Rs
    machine_code += MIPS_REGISTERS[rs]
    
    # Append Rt
    machine_code += MIPS_REGISTERS[rt]

    # Append Rd
    machine_code += MIPS_REGISTERS[rd]

    # Append shamt
    machine_code += shamt

    # Append func
    machine_code += func

    return machine_code     # 32-bit binary string

def GenerateBinaryForI(line):
    """
    Generate the binary representation of an I-type MIPS instruction.

    Args:
        line (str): A single line string representing the I-type instruction
                    in the format "instruction rt, rs, imm" or "instruction rt, imm(rs)".

    Returns:
        str: A 32-bit binary string representing the machine code of the given I-type instruction.

    Example:
        line = "addi $t1, $t2, 10"
        result = GenerateBinaryForI(line)
        # result should be a 32-bit binary string.
    """
    machine_code = ""

    tokens = line.split(" ")

    # INSTRUCTION_DECODED[instruction] = ['Type', 'Opcode', 'Func']
    # Func will be "N/A" for I-Type
    type, opcode, func = INSTRUCTION_DECODED[tokens[0]]

    # Delete comma
    for idx, token in enumerate(tokens):
        if "," in token:
            tokens[idx] = tokens[idx].replace(",", "")

    # Tokens could have either 3 parts or 4 parts
    # 3 parts: instruction rt, imm(rs)
    # 4 parts: instruction instruction rt, rs, imm

    rt = MIPS_REGISTERS[tokens[1]]
    if len(tokens) == 4:
        rs = MIPS_REGISTERS[tokens[2]]
        # Check if the 4th part is label or number
        if IsNumber(tokens[3]):
            immediate = DecimalToBinary(int(tokens[3]))
            immediate = immediate[16:]  # Take the 16 least significant bits
            machine_code += opcode + rs + rt + immediate
        else:
            label_address_hex = LABELS_TABLE[tokens[3]]
            _32_bits_binary_address = HexToBinary(label_address_hex)
            # Shift right 2 bits
            _30_bit_binary_address = _32_bits_binary_address[:-2]
            # Take the 16 least sinificant bits
            immediate = _30_bit_binary_address[14:]
            machine_code += opcode + rs + rt + immediate
    else:
        # Regular expression to extract the optional immediate value and the register
        match = re.search(r"(\d*)\((\$\w+)\)", tokens[2])
        if match:
            immediate = match.group(1)
            register = match.group(2)
            rs = MIPS_REGISTERS[register]
            
            # If we have the immediate
            if immediate:
                immediate = DecimalToBinary(int(immediate))
                immediate = immediate[16:]  # Take the 16 least significant bits
                machine_code += opcode + rs + rt + immediate
            else:
                # Have no number means it will be '0'
                immediate = DecimalToBinary(0)
                immediate = immediate[16:]  # Take the 16 least significant bits
                machine_code += opcode + rs + rt + immediate

    return machine_code     # 32-bit binary string

def GenerateBinaryForJ(line):
    """
    Generate the binary representation of a J-type MIPS instruction.

    Args:
        line (str): A single line string representing the J-type instruction
                    in the format "instruction label".

    Returns:
        str: A 32-bit binary string representing the machine code of the given J-type instruction.

    Example:
        line = "j label"
        result = GenerateBinaryForJ(line)
        # result should be a 32-bit binary string.
    """
    # J-Type instruction
    # instruction label
    # index:    0,    1, 

    # Machine code = Opcode + Immediate
    machine_code = ""

    tokens = line.split(" ")

    # INSTRUCTION_DECODED[key] = ['Type', 'Opcode', 'Func']
    # Func will be "N/A" for J-Type
    type, opcode, func = INSTRUCTION_DECODED[tokens[0]]

    # Delete comma
    for idx, token in enumerate(tokens):
        if "," in token:
            tokens[idx] = tokens[idx].replace(",", "")

    instruction, label = tokens
    label_address_hex = LABELS_TABLE[label] # Results is in Hex
    label_address_binary = HexToBinary(label_address_hex)

    # Shift right 2 bits, remains 30 bits
    label_address_binary = label_address_binary[:-2]
    # Take 26 least significant bits
    label_address_binary = label_address_binary[4:]

    # Append the opcode to the machine code string
    machine_code += opcode

    # Append label address 26-bit
    machine_code += label_address_binary

    return machine_code     # 32-bit binary string
