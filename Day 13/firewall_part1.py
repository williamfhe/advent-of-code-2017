
firewall = dict()

with open("input.txt") as f:
    for line in f.readlines():
        splitted = line.rstrip('\n').split()
        layer = int(splitted[0][:-1])
        size = int(splitted[1])
        firewall[layer] = size

pos = 0
severity = 0
last_layer = max(firewall.keys())

while pos <= last_layer:
    size = firewall.get(pos, 0)
    if size:
        if pos % (2 * (size - 1)) == 0:
            severity += pos * size
    pos += 1

print(severity)
