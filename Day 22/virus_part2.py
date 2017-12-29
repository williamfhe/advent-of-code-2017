from collections import defaultdict

up = (0, -1)
right = (+1, 0)
bot = (0, +1)
left = (-1, 0)

def init_cell():
    return 'c'

def change_dir(direction, cell_state):
    if cell_state == 'i':
        if direction == up:
            return right
        elif direction == right:
            return bot
        elif direction == bot:
            return left
        else:
            return up
    elif cell_state == 'c':
        if direction == up:
            return left
        elif direction == left:
            return bot
        elif direction == bot:
            return right
        else:
            return up
    elif cell_state == 'f':
        if direction == up:
            return bot
        elif direction == bot:
            return up
        elif direction == right:
            return left
        else:
            return right

    return direction

cells = defaultdict(init_cell)

with open("input.txt") as f:
    lines = f.read().splitlines()
    size = len(lines)
    for y, row in enumerate(lines):
        for x, cell in enumerate(row):
            if cell == '#':
                cells[(x, y)] = 'i'

x, y = size // 2, size // 2
direction = up
infected = 0

for _ in range(10000000):
    cell = cells[(x, y)]

    if cell == 'c':
        cells[(x, y)] = 'w'
    elif cell == 'w':
        cells[(x, y)] = 'i'
        infected += 1
    elif cell == 'i':
        cells[(x, y)] = 'f'
    else:
        cells[(x, y)] = 'c'

    direction = change_dir(direction, cell)

    x += direction[0]
    y += direction[1]

print(infected)
