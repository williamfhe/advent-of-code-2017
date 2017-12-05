entry = 289326

x, y = 0, 0
x_step = +1
y_step = 0

spiral = {(0, 0): 1}

value = 0

while value <= entry:
    x += x_step
    y += y_step
    
    value = 0

    for i in (-1, 0, +1):
        for j in (-1, 0, +1):
            value += spiral.get((x + i, y + j), 0)

    spiral[(x, y)] = value

    # print(x, y)
    if x == y and x > 0:
        # print("-x")
        x_step, y_step = -1, 0
    if x == y and x < 0:
        # print("+x")
        x_step, y_step = +1, 0
    if x == -y and x < 0:
        # print("-y")
        x_step, y_step = 0, -1
    if x == -(y - 1) and x > 0:
        # print("+y")
        x_step, y_step = 0, +1

print(value)