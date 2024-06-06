from config import *

def HexToDecimal(hex_string):
    # Remove the '0x' prefix if it exists
    if hex_string.startswith("0x"):
        hex_string = hex_string[2:]
    # Convert the hex string to an integer
    decimal_num = int(hex_string, 16)
    
    return decimal_num

def DecimalToHex(decimal_num):
    # Convert the decimal num to to hex string (32-bit)
    hex_string = hex(decimal_num & 0xFFFFFFFF)  # Ensure 32 bits

    # Remove prefix '0x'
    hex_string = hex_string[2:]

    # Prepend 0s to become the standardized form of 32-bit hex string (8 characters in length)
    hex_string = hex_string.zfill(8)

    return "0x" + hex_string

def DecimalToBinary(decimal_num):
    # Convert the decimal number to a 32-bit binary string
    if decimal_num < 0:
        # Make sure 32 bits represented
        binary_string = bin(decimal_num & 0xFFFFFFFF)
        # Remove "0b"
        binary_string = binary_string[2:]
    else:
        # Turn into 32 bits and remove "0b"
        binary_string = bin(decimal_num)[2:]
        # Fill up until 32 bits
        binary_string = binary_string.zfill(32)
    return binary_string    # 32-bit binary string

def HexToBinary(hex_string):
    decimal_num = HexToDecimal(hex_string)

    return DecimalToBinary(decimal_num)

def IsNumber(str_check):
    try:
        int(str_check)  # Error will occur if str_check is not a number
        return True
    except ValueError:
        # int() has errors, return False
        return False