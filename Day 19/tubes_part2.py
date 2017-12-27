
with open("input.txt") as f:
    path = [line.rstrip('\n') for line in f.readlines()]

north = (0, -1)
east = (+1, 0)
south = (0, +1)
west = (-1, 0)

direction = south

x, y = path[0].index('|'), 0
current_char = '|'

steps = 0

while current_char != ' ':
    current_char = path[y][x]

    if current_char == '+':
        if direction in (south, north):
            if path[y][x - 1] != ' ':
                direction = west
            else:
                direction = east
        else:
            if path[y - 1][x] != ' ':
                direction = north
            else:
                direction = south
    
    x += direction[0]
    y += direction[1]
    steps += 1

print(steps - 1)
