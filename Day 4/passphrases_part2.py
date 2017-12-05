
def is_valid_passphrase(phrase):
    """ Return 1 if the phrase is a valid passphrase else 0 """
    counter_dict = dict()
    for word in phrase.split(" "):
        if has_anagram(counter_dict, word):
            return 0
        else:
            counter_dict[word] = 1
    return 1

def has_anagram(counter_dict, word):
    """ Return True if the word has an anagram in the dictionnary else False"""
    for w in counter_dict:
        if sorted(w) == sorted(word):
            return True
    return False

valid = 0
with open("input.txt") as f:
    for phrase in f.readlines():
        valid += is_valid_passphrase(phrase[:-1])

print(valid)
