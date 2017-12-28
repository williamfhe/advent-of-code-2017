
def abs_v(vec):
    return abs(vec[0]) + abs(vec[1]) + abs(vec[2])

with open("input.txt") as f:
    for i, line in enumerate(f.readlines()):
        splitted = line.rstrip('\n').split()
        acc = [int(num) for num in splitted[2][3:-1].split(',')]
        
        p_acc = abs_v(acc)

        if i == 0:
            min_p = 0
            min_acc = p_acc
        else:
            if p_acc < min_acc:
                min_p = i
                min_acc = p_acc

print(min_p)
