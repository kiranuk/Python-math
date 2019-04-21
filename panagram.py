import string
from collections import OrderedDict


def panagram(s):
    l = s.lower()
    l = list(l)
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    counter = 0
    d1 = {}
    for i in alphabet:
        d1[i] = 0
        for j in l:
            r = l.count(j)
            d1[j] = r
        if d1[i] > 0:
            return True
        else:
            return False


print(panagram("This is nice word"))
print(panagram("Jived fox nymph grabs quick waltz"))
print(panagram("Jived fox nymph grabs quick waltz"))
