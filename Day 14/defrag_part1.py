from knot_hash import knot_hash

entry = "ljoxqyyw"
total = 0
for i in range(128):
    hashed = bin(int(knot_hash(f"{entry}-{i}"), 16))[2:]
    total += hashed.count('1')

print(total)
