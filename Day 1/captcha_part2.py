with open("input.txt") as f:
    entry = f.readline()

length = len(entry)
total = 0

step = length // 2

for i in range(length):
    if entry[i] == entry[(i + step) % length]:
        total += int(entry[i])

print(total)
