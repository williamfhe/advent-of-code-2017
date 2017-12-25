from knot_hash import knot_hash

def propagate(disk, seen, i, j):
    if disk[i][j] == '0' or (i, j) in seen:
        return
    seen.add((i, j))
    if i > 0:
        propagate(disk, seen, i - 1, j)
    if i < 127:
        propagate(disk, seen, i + 1, j)
    if j > 0:
        propagate(disk, seen, i, j - 1)
    if j < 127:
        propagate(disk, seen, i, j + 1)


entry = "ljoxqyyw"
disk = list()
for i in range(128):
    hashed = bin(int(knot_hash(f"{entry}-{i}"), 16))[2:].zfill(128)
    disk.append(hashed)


regions_count = 0
seen = set()
for i in range(128):
    for j in range(128):
        if disk[i][j] == '1' and (i, j) not in seen:
            propagate(disk, seen, i, j)
            regions_count += 1

print(regions_count)
