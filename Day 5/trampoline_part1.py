
with open("input.txt") as f:
    entry = [int(line) for line in f.readlines()]

steps = 0
current_pos = 0
length = len(entry)

while current_pos < length:
    old = current_pos
    current_pos += entry[current_pos]
    entry[old] += 1
    steps += 1

print(steps)
