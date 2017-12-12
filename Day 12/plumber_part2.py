
def check_programs(programs, contained, program_name):
    for name in programs[program_name]:
        name = name.rstrip(',')
        if name not in contained:
            contained.add(name)
            contained = check_programs(programs, contained, name)
    
    return contained

programs = dict()

with open("input.txt") as f:
    for line in f.readlines():
        splitted = line.rstrip('\n').split()
        name = splitted[0]
        connections = splitted[2:]
        programs[name] = connections

all_prog_in_groups = set()
group_count = 0

for prog_name in programs:
    if prog_name not in all_prog_in_groups:
        contained = set()
        contained.add(prog_name)
        contained = check_programs(programs, contained, prog_name)
        all_prog_in_groups.update(contained)
        group_count += 1

print(group_count)
