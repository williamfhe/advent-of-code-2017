
def check_programs(programs, contained, program_name):
    for name in programs[program_name]:
        name = name.rstrip(',')
        if name not in contained:
            contained.add(name)
            contained = check_programs(programs, contained, name)
    
    return contained

programs = dict()
contained = set('0')

with open("input.txt") as f:
    for line in f.readlines():
        splitted = line.rstrip('\n').split()
        name = splitted[0]
        connections = splitted[2:]
        programs[name] = connections

contained = check_programs(programs, contained, '0')
print(len(contained))
