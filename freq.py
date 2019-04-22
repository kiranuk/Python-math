def freq(s):
    d = {}
    for i in s:
        l = s.count(i)
        d[i] = l
    return d
print(freq("references"))
