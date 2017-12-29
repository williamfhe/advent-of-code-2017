from collections import defaultdict

parts_dict = defaultdict(set)

with open("input.txt") as f:
    for line in f.readlines():
        splitted = line.rstrip('\n').split('/')
        part = int(splitted[0]), int(splitted[1])
        parts_dict[part[0]].add(part)
        parts_dict[part[1]].add(part)

def recurse_bridge(used, parts_dict, current):
    for part in parts_dict[current]:
        if part not in used:
            used_copy = used.copy()
            used_copy.add(part)
            cur = part[1] if part[0] == current else part[0]
            yield from recurse_bridge(used_copy, parts_dict, cur)
    yield used

all_bridges = [size for size in recurse_bridge(set(), parts_dict, 0)]
max_strengh = max(map(lambda bridge: sum([a + b for a, b in bridge]), all_bridges))
print(max_strengh)
