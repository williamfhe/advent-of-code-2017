
dirs = {
    "n": (0, +1, -1),
    "nw": (-1, 1, 0),
    "ne": (1, 0, -1),
    "se": (1, -1, 0),
    "s": (0, -1, 1),
    "sw": (-1, 0, 1)
}

with open("input.txt") as f:
    entry = f.readline().split(',')

x, y, z = 0, 0, 0

max_steps = 0

for move in entry:
    xx, yy, zz = dirs[move]
    x += xx
    y += yy
    z += zz
    steps = (abs(x) + abs(y) + abs(z)) // 2
    max_steps = max(max_steps, steps)

print(max_steps)
