from collections import defaultdict

def get_value(v, registers):
    if v.isalpha():
        return registers[v]
    return int(v)

registers = defaultdict(int)

with open("input.txt") as f:
    instructions = [line.rstrip('\n').split() for line in f.readlines()]

current_pos = 0
total_instructions = len(instructions)
mul_count = 0

while current_pos < total_instructions:
    instr = instructions[current_pos]
    reg = instr[1]
    
    if instr[0] == "set":
        registers[reg] = get_value(instr[2], registers)
    elif instr[0] == "sub":
        registers[reg] -= get_value(instr[2], registers)
    elif instr[0] == "mul":
        registers[reg] *= get_value(instr[2], registers)
        mul_count += 1
    elif instr[0] == "jnz":
        if get_value(reg, registers) != 0:
            current_pos += get_value(instr[2], registers) - 1

    current_pos += 1

print(mul_count)
