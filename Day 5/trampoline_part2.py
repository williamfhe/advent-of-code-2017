
with open("input.txt") as f:
    entry = [int(line) for line in f.readlines()]

steps = 0
current_pos = 0
length = len(entry)

while current_pos < length:
    old = current_pos
    jump = entry[current_pos]
    current_pos += jump
    if jump >= 3:
        entry[old] -= 1
    else:
        entry[old] += 1
    steps += 1

print(steps)
