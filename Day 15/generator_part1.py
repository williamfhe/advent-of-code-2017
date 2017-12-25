
val_a = 699
val_b = 124

n = 40_000_000  # 40 million

count = 0

for _ in range(n):
    val_a = (val_a * 16807) % 2147483647
    val_b = (val_b * 48271) % 2147483647

    if val_a & 0xffff == val_b & 0xffff:
        count += 1

print(count)
