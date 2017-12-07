disc_in_use = dict()
all_disc = list()

with open("input.txt") as f:
    for line in f.readlines():
        splitted = line.rstrip('\n').split(" ")
        if len(splitted) < 3:
            continue
        all_disc.append(splitted[0])
        for disc in splitted[3:]:
            disc_in_use[disc.rstrip(',')] = 1

for disc in all_disc:
    if disc not in disc_in_use:
        print(disc)
        break
