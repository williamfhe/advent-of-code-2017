# I choosed to not use eval

def exec_condition(splitted_line):
    register_name = splitted_line[0]
    action = splitted_line[1]

    cond_action_value = int(splitted_line[2])

    cond_register = splitted_line[4]
    cond = splitted_line[5]
    cond_value = int(splitted_line[6])

    if action == "dec":
        cond_action_value = -cond_action_value

    actual_register_value = registers.get(register_name, 0)
    cond_register_value = registers.get(cond_register, 0)
    
    if is_condition_valid(cond, cond_register_value, cond_value):
        actual_register_value += cond_action_value
    
    registers[register_name] = actual_register_value

def is_condition_valid(condition, value1, value2):
    condition_valid = False
    if condition == ">":
        condition_valid = value1 > value2
    elif condition == "<":
        condition_valid = value1 < value2
    elif condition == ">=":
        condition_valid = value1 >= value2
    elif condition == "<=":
        condition_valid = value1 <= value2
    elif condition == "==":
        condition_valid = value1 == value2
    elif condition == "!=":
        condition_valid = value1 != value2

    return condition_valid

registers = dict()

highest_value_held = 0

with open("input.txt") as f:
    for line in f.readlines():
        splitted = line.rstrip('\n').split(" ")
        exec_condition(splitted)
        highest_value_held = max(highest_value_held, max(registers.values()))

print(highest_value_held)
