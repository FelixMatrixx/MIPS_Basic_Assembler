import re
from config import *
from number_manipulate import *
from generate_machine_code import *

def ReadFile(filename):
    lines = []
    try:    
        # Open File
        input_file = open(filename)

        while input_file:
            line = input_file.readline()
            if line == "":
                break
            lines.append(line)

        # Close File
        input_file.close()

        return lines
    except Exception as e:
        print(f"An error occurred: {e}")

def WriteFile(filename, lines):
    try:
        output_file = open(filename, "w")
        for line in lines:
            output_file.write(line + "\n")
    except Exception as e:
        print(f"An error occurred: {e}")

def DeleteComment(lines):
    # Delete space before and after line
    COMMENT_PATTERN = r'#.+'

    # Remove comment
    removed_comment_lines = [re.sub(COMMENT_PATTERN, '', line) for line in lines]
    
    # Get rid of white space
    space_free_lines = [line.strip() for line in removed_comment_lines]

    # Get rid of empty line
    processed_lines = [line for line in space_free_lines if line != ""]
    
    return processed_lines

def BuiltLabelTable(lines):
    label_table = dict()
    current_address = ROOT_ADDRESS_DEC
    for line in lines:
        if ":" in line:
            label, instruction = line.split(":", 1)
            LABELS_TABLE[label.strip()] = DecimalToHex(current_address)
        else:
            current_address += INSTRUCTION_OFFSET   # Each instruction is 4 bytes in length
    
    print("Building Label Table succeed!!!")

    return

def DeleteLabel(lines):
    non_label_lines = [line for line in lines if ":" not in line]
    return non_label_lines

def GetType(line):
    # Split into smaller components
    tokens = line.split(" ", 1)      # Split at the first space (there will be no space before the instruction)
    instruction = tokens[0]          # The first token is instruction
    type, opcode, func = INSTRUCTION_DECODED[instruction]    # (list) ['Type', 'Opcode', 'Func']
    return type            # Return the Type

def FirstPass(lines):
    # Get rid of comment and empty lines
    comment_deleted_lines = DeleteComment(lines)
    # Form A Hash Table of labels
    # LABELS_TABLE is a global dictionary
    BuiltLabelTable(comment_deleted_lines)
    non_label_lines = DeleteLabel(comment_deleted_lines)

    print("First Pass completed!!!")
    return non_label_lines

def SecondPass(lines):
    # A list store all machine code
    machine_code_lines = list()

    for line in lines:
        type = GetType(line)
        machine_code_line = str()
        if type == "R":
            machine_code_line = GenerateBinaryForR(line)
        elif type == "I":
            machine_code_line = GenerateBinaryForI(line)
        else:
            machine_code_line = GenerateBinaryForJ(line)

        machine_code_lines.append(machine_code_line)

    print("Second Pass completed!!!")
    return machine_code_lines # A list of all instructions' machine code