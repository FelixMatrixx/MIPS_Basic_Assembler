HEX_STRING_32_BIT_LENGTH = 8
ROOT_ADDRESS_HEX = "0x00400000"
ROOT_ADDRESS_DEC = 4194304
INSTRUCTION_OFFSET = 4

LABELS_TABLE = dict()

INSTRUCTION_DECODED = {'add': ['R', '000000', '100000'],
           'addu': ['R', '000000', '100001'],
           'and': ['R', '000000', '100100'],
           'jr': ['R', '000000', '001000'],
           'addi': ['I', '001000', 'N/A'],
           'addiu': ['I', '001001', 'N/A'],
           'andi': ['I', '001100', 'N/A'],
           'beq': ['I', '000100', 'N/A'],
           'bne': ['I', '000101', 'N/A'],
           'lbu': ['I', '100100', 'N/A'],
           'lhu': ['I', '100101', 'N/A'],
           'lui': ['I', '001111', 'N/A'],
           'lw': ['I', '100011', 'N/A'],
           'sw': ['I', '101011', 'N/A'],
           'j': ['J', '000010', 'N/A'],
           'jal': ['J', '000011', 'N/A']
}

MIPS_REGISTERS = {
    '$zero': '00000',
    '$at': '00001',
    '$v0': '00010',
    '$v1': '00011',
    '$a0': '00100',
    '$a1': '00101',
    '$a2': '00110',
    '$a3': '00111',
    '$t0': '01000',
    '$t1': '01001',
    '$t2': '01010',
    '$t3': '01011',
    '$t4': '01100',
    '$t5': '01101',
    '$t6': '01110',
    '$t7': '01111',
    '$s0': '10000',
    '$s1': '10001',
    '$s2': '10010',
    '$s3': '10011',
    '$s4': '10100',
    '$s5': '10101',
    '$s6': '10110',
    '$s7': '10111',
    '$t8': '11000',
    '$t9': '11001',
    '$k0': '11010',
    '$k1': '11011',
    '$gp': '11100',
    '$sp': '11101',
    '$fp': '11110',
    '$ra': '11111'
}