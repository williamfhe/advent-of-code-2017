step = 359
pos = 0
val = -1

for i in range(1, 50_000_001):
    pos = (pos + step) % i + 1
    if pos == 1:
        val = i

print(val)
