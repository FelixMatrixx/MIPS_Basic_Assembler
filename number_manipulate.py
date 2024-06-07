from config import *

def HexToDecimal(hex_string):
    """
    Convert a hexadecimal string to a decimal integer.

    Args:
        hex_string (str): A string representing a hexadecimal number. The string can optionally start with '0x'.

    Returns:
        int: The decimal integer representation of the hexadecimal string.

    Example:
        hex_string = "0x1A"
        result = HexToDecimal(hex_string)
        # result should be 26
    """
    # Remove the '0x' prefix if it exists
    if (hex_string.startswith("0x")):
        hex_string = hex_string[2:]
    # Convert the hex string to an integer
    decimal_num = int(hex_string, 16)
    
    return decimal_num

def DecimalToHex(decimal_num):
    """
    Convert a decimal integer to a hexadecimal string (32-bit).

    Args:
        decimal_num (int): A decimal integer.

    Returns:
        str: The hexadecimal string representation of the decimal integer, prefixed with '0x' and padded to 8 characters.

    Example:
        decimal_num = 26
        result = DecimalToHex(decimal_num)
        # result should be "0x0000001a"
    """
    # Convert the decimal num to to hex string (32-bit)
    hex_string = hex(decimal_num & 0xFFFFFFFF)  # Ensure 32 bits

    # Remove prefix '0x'
    hex_string = hex_string[2:]

    # Prepend 0s to become the standardized form of 32-bit hex string (8 characters in length)
    hex_string = hex_string.zfill(8)

    return "0x" + hex_string

def DecimalToBinary(decimal_num):
    """
    Convert a decimal integer to a 32-bit binary string.

    Args:
        decimal_num (int): A decimal integer.

    Returns:
        str: The 32-bit binary string representation of the decimal integer.

    Example:
        decimal_num = 26
        result = DecimalToBinary(decimal_num)
        # result should be "00000000000000000000000000011010"
    """
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
    """
    Convert a hexadecimal string to a 32-bit binary string.

    Args:
        hex_string (str): A string representing a hexadecimal number. The string can optionally start with '0x'.

    Returns:
        str: The 32-bit binary string representation of the hexadecimal number.

    Example:
        hex_string = "0x1A"
        result = HexToBinary(hex_string)
        # result should be "00000000000000000000000000011010"
    """
    decimal_num = HexToDecimal(hex_string)
    return DecimalToBinary(decimal_num)

def IsNumber(str_check):
    """
    Check if a string represents a number.

    Args:
        str_check (str): A string to check.

    Returns:
        bool: True if the string represents a number, False otherwise.

    Example:
        str_check = "123"
        result = IsNumber(str_check)
        # result should be True
    """
    try:
        int(str_check)  # Error will occur if str_check is not a number
        return True
    except ValueError:
        # int() has errors, return False
        return False
