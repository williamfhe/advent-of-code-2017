
def is_prime(number):
    for n in range(2, number):
        if number % n == 0:
            return False
    return True

b = 99 # input

# Start
b = b * 100 + 100000
c = b + 17000

h = 0
for i in range(b, c + 1, 17):
    if not is_prime(i):
        h += 1

print(h)
