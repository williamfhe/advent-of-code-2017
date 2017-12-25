
def generator(val, factor, crit):
    while True:
        val = (val * factor) % 2147483647
        if not val % crit:
            yield val


val_a = generator(699, 16807, 4)
val_b = generator(124, 48271, 8)

n = 5_000_000  # 5 million

count = 0

for _ in range(n):
    if next(val_a) & 0xffff == next(val_b) & 0xffff:
        count += 1

print(count)
