with open("input.txt") as f:
    entry = f.readline()

length = len(entry)
total = 0


for i in range(length):
    if entry[i] == entry[(i + 1) % length]:
        total += int(entry[i])

print(total)
