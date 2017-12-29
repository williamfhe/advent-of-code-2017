from collections import defaultdict

up = (0, -1)
right = (+1, 0)
bot = (0, +1)
left = (-1, 0)

def change_dir(direction, going_right):
    if going_right:
        if direction == up:
            return right
        elif direction == right:
            return bot
        elif direction == bot:
            return left
        else:
            return up
    else:
        if direction == up:
            return left
        elif direction == left:
            return bot
        elif direction == bot:
            return right
        else:
            return up

cells = defaultdict(bool)
with open("input.txt") as f:
    lines = f.read().splitlines()
    size = len(lines)
    for y, row in enumerate(lines):
        for x, cell in enumerate(row):
            if cell == '#':
                cells[(x, y)] = True

x, y = size // 2, size // 2
direction = up
infected = 0

for _ in range(10000):
    cell = cells[(x, y)]
    if cell:
        cells[(x, y)] = False
    else:
        infected += 1
        cells[(x, y)] = True
    
    direction = change_dir(direction, cell)

    x += direction[0]
    y += direction[1]

print(infected)
