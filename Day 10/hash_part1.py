entry = [18, 1, 0, 161, 255, 137, 254, 252, 14, 95, 165, 33, 181, 168, 2, 188]

pos = 0

size = 256
skip = 0
numbers = [i for i in range(size)]


for length in entry:
    end = pos + length
    if end >= size:
        to_reverse = numbers[pos:size] + numbers[0:end - size]
    else:
        to_reverse = numbers[pos:end]

    i = pos
    for number in reversed(to_reverse):
        numbers[i] = number
        i = (i + 1) % size

    pos = (pos + length + skip) % size
    skip += 1

print(numbers[0] * numbers[1])
