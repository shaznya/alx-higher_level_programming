#!/usr/bin/python3
import dis

def magic_calculation(a, b):
    result = b**a + 98
    return result
disassembly = dis.Bytecode(magic_calculation)
for instruction in disassembly:
    print(instruction)
