step = 359
spinlock = [0]
pos = 0

for i in range(1, 2018):
    pos = (pos + step) % i + 1
    spinlock.insert(pos, i)

print(spinlock[(pos + 1) % 2018])
