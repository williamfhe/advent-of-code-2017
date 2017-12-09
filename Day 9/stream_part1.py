with open("input.txt") as f:
    entry = f.readline()

level = 0
garbage = False
ignored = False

groups = list()

for c in entry:
    if ignored:
        ignored = False
    elif c == '!':
        ignored = True
    elif garbage:
        if c == '>':
            garbage = False
    elif c == '<':
        garbage = True
    elif c == '{':
        level += 1
    elif c == '}':
        groups.append(level)
        level -= 1

print(sum(groups))
