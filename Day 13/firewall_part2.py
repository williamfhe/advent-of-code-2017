def caught_in_firewall(firewall, last_layer, delay):
    for pos in range(last_layer + 1):
        size = firewall.get(pos, 0)
        if size:
            if (delay + pos) % (2 * (size - 1)) == 0:
                return True 
    return False

firewall = dict()

with open("input.txt") as f:
    for line in f.readlines():
        splitted = line.rstrip('\n').split()
        layer = int(splitted[0][:-1])
        size = int(splitted[1])
        firewall[layer] = size

last_layer = max(firewall.keys())
delay = 0

while caught_in_firewall(firewall, last_layer, delay):
    delay += 1

print(delay)
