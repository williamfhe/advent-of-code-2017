class Disc:
    def __init__(self, name, weight, childs_names):
        self.name = name
        self.weight = weight
        self.childs_names = childs_names
        self.total_weight = 0

def recurse_childs_weights(disc):
    if not disc.childs_names:
        disc.total_weight = disc.weight
        return disc

    childs = list()
    total_weight = disc.weight
    for child_name in disc.childs_names:
        child = all_discs[child_name]
        child = recurse_childs_weights(child)
        total_weight += child.total_weight

        childs.append(child)

    disc.total_weight = total_weight
    weights = [child.total_weight for child in childs]

    if len(set(weights)) == 1:
        return disc

    imbalenced_weight = min(set(weights), key=weights.count)
    wanted_weight = max(set(weights), key=weights.count)
    correction = wanted_weight - imbalenced_weight

    imbalenced_child = [child for child in childs if child.total_weight == imbalenced_weight][0]
    corrected_weight = imbalenced_child.weight + correction

    print(imbalenced_child.name, "should weight:", corrected_weight)

    return disc


all_discs = dict()

with open("input.txt") as f:
    for line in f.readlines():
        splitted = line.rstrip('\n').split(" ")
        name = splitted[0]
        weight = int(splitted[1][1:-1])
        childs_names = [d.rstrip(',') for d in splitted[3:]]

        all_discs[name] = Disc(name, weight, childs_names)


bottom_name = "veboyvy"  # Know because of part 1

recurse_childs_weights(all_discs[bottom_name])
