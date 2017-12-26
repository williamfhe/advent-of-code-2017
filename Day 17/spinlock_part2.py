step = 359
pos = 0

val = -1

n = 50_000_000 + 1

for i in range(1, n):
    pos = (pos + step) % i + 1
    if pos == 1:
        val = i

print(val)
