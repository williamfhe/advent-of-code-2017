from collections import defaultdict

class Program:
    def __init__(self, pid):
        self.registers = defaultdict(int)
        self.registers['p'] = pid
        self.queue = []
        self.waiting = False
        self.instr_pos = 0

def get_value(v, program):
    if v.isalpha():
        return program.registers[v]
    return int(v)

def swap_program(current_prog):
    return 0 if current_prog else 1


with open("input.txt") as f:
    instructions = [line.rstrip('\n').split() for line in f.readlines()]

prog_0 = Program(0)
prog_1 = Program(1)

programs = [prog_0, prog_1]

cur_prog = 0
total_instructions = len(instructions)

total_send = 0

while prog_0.instr_pos < total_instructions and prog_1.instr_pos < total_instructions:
    prog = programs[cur_prog]
    instr = instructions[prog.instr_pos]
    reg = instr[1]

    if prog_0.waiting and prog_1.waiting and not (prog_0.queue or prog_1.queue):
        break

    if instr[0] == "set":
        prog.registers[reg] = get_value(instr[2], prog)
    elif instr[0] == "add":
        prog.registers[reg] += get_value(instr[2], prog)
    elif instr[0] == "mul":
        prog.registers[reg] *= get_value(instr[2], prog)
    elif instr[0] == "mod":
        prog.registers[reg] %= get_value(instr[2], prog)
    elif instr[0] == "jgz":
        if get_value(reg, prog) > 0:
            prog.instr_pos += get_value(instr[2], prog) - 1

    elif instr[0] == "snd":
        if cur_prog == 1:
            total_send += 1
        val = get_value(reg, prog)
        programs[swap_program(cur_prog)].queue.append(val)
    elif instr[0] == "rcv":
        if prog.queue:  # not empty
            prog.waiting = False
            rcv_value = prog.queue.pop(0)
            prog.registers[reg] = rcv_value
        else:
            prog.waiting = True
            cur_prog = swap_program(cur_prog)
            continue

    prog.instr_pos += 1

print(total_send)
