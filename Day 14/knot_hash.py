
def knot_hash(text):
    entry = [ord(c) for c in text]
    entry += [17, 31, 73, 47, 23]
    numbers = list(range(256))
    pos = skip = 0
    for _ in range(64):
        for length in entry:
            end = pos + length
            if end >= 256:
                to_reverse = numbers[pos:256] + numbers[0:end - 256]
            else:
                to_reverse = numbers[pos:end]

            i = pos
            for number in reversed(to_reverse):
                numbers[i] = number
                i = (i + 1) % 256

            pos = (pos + length + skip) % 256
            skip += 1

    dense_hash = ""

    for i in range(16):
        start = i * 16
        x = numbers[start]
        for j in range(1, 16):
            x ^= numbers[start + j]
        dense_hash += '%02x' % x

    return dense_hash
