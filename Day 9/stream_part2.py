with open("input.txt") as f:
    entry = f.readline()
    
garbage = False
ignored = False

garbage_count = 0

for c in entry:
    if ignored:
        ignored = False
    elif c == '!':
        ignored = True
    elif garbage:
        if c == '>':
            garbage = False
        else:
            garbage_count += 1
    elif c == '<':
        garbage = True

print(garbage_count)