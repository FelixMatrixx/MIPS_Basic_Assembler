from config import *
from utils import *

def main():
    print("======================")
    lines = ReadFile("mips_instruction.txt")
    # Delete comments, white spaces, labels and empty lines
    processed_lines = FirstPass(lines)

    # Temporary file to store precessed lines
    WriteFile("cleaned_instruction.txt", processed_lines)
    
    machine_code_lines = SecondPass(processed_lines)
    WriteFile("machine_code.txt", machine_code_lines)
    print("Program stopped....")

if __name__ == "__main__":
    main()
