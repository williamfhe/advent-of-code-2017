
def is_valid_passphrase(phrase):
    """ Return 1 if the phrase is a valid passphrase else 0 """
    counter_dict = dict()
    for word in phrase.split(" "):
        if word in counter_dict:
            return 0
        else:
            counter_dict[word] = 1
    return 1

valid = 0
with open("input.txt") as f:
    for phrase in f.readlines():
        valid += is_valid_passphrase(phrase[:-1])

print(valid)
