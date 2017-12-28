
def get_enhancement(fractal, enhancements, i, j, block_size):
    part = [fractal[i][j:j+block_size] for i in range(i, i+block_size)]
    for _ in range(4):
        enhanced = enhancements.get("".join(flip(part)), None)
        if enhanced:
            return enhanced
        part = rotate(part)
        enhanced = enhancements.get("".join(part), None)
        if enhanced:
            return enhanced

def flip(part):
    return [row[::-1] for row in part]

def rotate(part):
    n_part = []
    size = len(part)
    for i in range(size):
        row = ""
        for j in range(size):
            row += part[size - j - 1][i]
        n_part.append(row)
    return n_part
    
def iteration(fractal, enhancements):
    size = len(fractal)
    if size % 2 == 0:
        n_size = (size // 2) * 3
        n_block_size = 3
        block_size = 2
    else:
        n_size = (size // 3) * 4
        n_block_size = 4
        block_size = 3
    
    n_fractal = ["" for i in range(n_size)]

    for i in range(size // block_size):
        for j in range(size // block_size):
            enhanced = get_enhancement(fractal, enhancements, i * block_size, j * block_size, block_size)
            for e, part in enumerate(enhanced):
                n_fractal[i * n_block_size + e] += part

    return n_fractal

enhancements = dict()

with open("input.txt") as f:
    for line in f.readlines():
        splitted = line.split()
        original = splitted[0].replace('/', '')
        enhanced = splitted[2].split('/')
        enhancements[original] = enhanced

fractal = ".#./..#/###".split("/")

for _ in range(18):
    fractal = iteration(fractal, enhancements)

total_on = "".join(fractal).count("#")
print(total_on)
