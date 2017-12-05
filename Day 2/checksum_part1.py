def line_to_int_array(line):
    line = line.replace(" ", ";")
    line = line.replace("\t", ";")
    return [int(token) for token in line.split(";")]

with open("input.txt") as f:
    entry = [line_to_int_array(line) for line in f.readlines()]

total = 0

for row in entry:
    total += max(row) - min(row)

print(total)
