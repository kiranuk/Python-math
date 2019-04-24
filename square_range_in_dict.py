def dict_of_square(n):
    d = {}
    for i in range(1, n+1):
        d[i] = i*i
    return d

print(dict_of_square(8))
