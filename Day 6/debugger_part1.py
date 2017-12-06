entry = [2, 8, 8, 5, 4, 2, 3, 1, 5, 5, 1, 2, 15, 13, 5, 14]

cached = dict()
length = len(entry)

current_pos = selected_bank = entry.index(max(entry))
steps = 0

while True:
    current_pos = (current_pos + 1) % length
    
    entry[selected_bank] -= 1

    if entry[selected_bank] == 0:
        entry[current_pos] += 1
        current_pos = selected_bank = entry.index(max(entry))
        steps += 1
        if tuple(entry) in cached:
            break
        cached[tuple(entry)] = 1
    else:
        entry[current_pos] += 1

print(steps)
