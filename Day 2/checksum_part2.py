def line_to_int_array(line):
    line = line.replace(" ", ";")
    line = line.replace("\t", ";")
    return [int(token) for token in line.split(";")]

def dividing_numbers(row):
    for number1 in row:
        for number2 in row[1:]:
            if number1 == number2:
                continue
            if number1 % number2 == 0:
                return number1 // number2
            if number2 % number1 == 0:
                return number2 // number1
    return 0

with open("input.txt") as f:
    entry = [line_to_int_array(line) for line in f.readlines()]

total = 0

for row in entry:
    total += dividing_numbers(row)

print(total)
