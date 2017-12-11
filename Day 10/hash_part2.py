
msg = "18,1,0,161,255,137,254,252,14,95,165,33,181,168,2,188"
entry = [ord(c) for c in msg]
entry += [17, 31, 73, 47, 23]

size = 256
numbers = [i for i in range(size)]

pos = 0
skip = 0

for _ in range(64):
    for length in entry:
        end = pos + length
        if end >= size:
            to_reverse = numbers[pos:size] + numbers[0:end - size]
        else:
            to_reverse = numbers[pos:end]

        i = pos
        for number in reversed(to_reverse):
            numbers[i] = number
            i = (i + 1) % size

        pos = (pos + length + skip) % size
        skip += 1

dense_hash = list()

for i in range(16):
    start = i * 16
    x = numbers[start]
    for j in range(1, 16):
        x ^= numbers[start + j]
    dense_hash.append('%02x' % x)

knot_hash = "".join(dense_hash)
print(knot_hash)
