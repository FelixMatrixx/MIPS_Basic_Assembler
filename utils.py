import re
from config import *
from number_manipulate import *
from generate_machine_code import *

def ReadFile(filename):
    """
    Read the contents of a file and return its lines as a list.

    Args:
        filename (str): The name of the file to read.

    Returns:
        list: A list of strings, each representing a line in the file.

    Example:
        lines = ReadFile("example.txt")
        # lines will contain the lines from "example.txt"
    """
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
    """
    Write the provided lines to a file.

    Args:
        filename (str): The name of the file to write to.
        lines (list): A list of strings, each representing a line to write to the file.

    Example:
        lines = ["Line 1", "Line 2"]
        WriteFile("example.txt", lines)
        # "example.txt" will contain "Line 1\nLine 2\n"
    """
    try:
        output_file = open(filename, "w")
        for line in lines:
            output_file.write(line + "\n")
        output_file.close()
    except Exception as e:
        print(f"An error occurred: {e}")

def DeleteComment(lines):
    """
    Remove comments and excess whitespace from a list of lines.

    Args:
        lines (list): A list of strings, each representing a line of code.

    Returns:
        list: A list of strings with comments and excess whitespace removed.

    Example:
        lines = ["code # comment", "   more code   "]
        result = DeleteComment(lines)
        # result will be ["code", "more code"]
    """
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
    """
    Build a table of labels and their corresponding addresses.

    Args:
        lines (list): A list of strings, each representing a line of code.

    Returns:
        None

    Example:
        lines = ["label1: instruction", "instruction"]
        BuiltLabelTable(lines)
        # LABELS_TABLE will be updated with {"label1": "0x00000000"}
    """
    label_table = dict()
    current_address = ROOT_ADDRESS_DEC
    for line in lines:
        if ":" in line:
            label, instruction = line.split(":", 1)
            LABELS_TABLE[label.strip()] = DecimalToHex(current_address)
        else:
            current_address += INSTRUCTION_OFFSET   # Each instruction is 4 bytes in length
    
    print("Building Label Table succeed!!!")

def DeleteLabel(lines):
    """
    Remove labels from a list of lines.

    Args:
        lines (list): A list of strings, each representing a line of code.

    Returns:
        list: A list of strings with labels removed.

    Example:
        lines = ["label1: instruction", "instruction"]
        result = DeleteLabel(lines)
        # result will be ["instruction"]
    """
    non_label_lines = [line for line in lines if ":" not in line]
    return non_label_lines

def GetType(line):
    """
    Get the type of a given instruction line.

    Args:
        line (str): A string representing a single line of code.

    Returns:
        str: The type of the instruction ("R", "I", or "J").

    Example:
        line = "add $t1, $t2, $t3"
        result = GetType(line)
        # result will be "R"
    """
    # Split into smaller components
    tokens = line.split(" ", 1)      # Split at the first space (there will be no space before the instruction)
    instruction = tokens[0]          # The first token is instruction
    type, opcode, func = INSTRUCTION_DECODED[instruction]    # (list) ['Type', 'Opcode', 'Func']
    return type            # Return the Type

def FirstPass(lines):
    """
    Perform the first pass on the lines of code to remove comments, build the label table, and remove labels.

    Args:
        lines (list): A list of strings, each representing a line of code.

    Returns:
        list: A list of strings with comments and labels removed.

    Example:
        lines = ["label1: instruction", "instruction # comment"]
        result = FirstPass(lines)
        # result will be ["instruction", "instruction"]
    """
    # Get rid of comment and empty lines
    comment_deleted_lines = DeleteComment(lines)
    # Form A Hash Table of labels
    # LABELS_TABLE is a global dictionary
    BuiltLabelTable(comment_deleted_lines)
    non_label_lines = DeleteLabel(comment_deleted_lines)

    print("First Pass completed!!!")
    return non_label_lines

def SecondPass(lines):
    """
    Perform the second pass on the lines of code to generate machine code.

    Args:
        lines (list): A list of strings, each representing a line of code.

    Returns:
        list: A list of strings, each representing the machine code of the corresponding line of code.

    Example:
        lines = ["add $t1, $t2, $t3", "beq $t1, $t2, label"]
        result = SecondPass(lines)
        # result will be a list of 32-bit binary strings
    """
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
