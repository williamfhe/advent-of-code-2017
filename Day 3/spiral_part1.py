entry = 289326

x, y = 0, 0
x_step = +1
y_step = 0

for i in range(1, entry):
    x += x_step
    y += y_step
    
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


print(abs(x) + abs(y))
    