def tables2(n):
    for i in range(1, n+1):
#        print("-"*(n*5))
        for j in range(1, n+1):
            if j == n:
                print("{:4}".format(i*j))
            else:
                print("{:4}".format(i*j), end=" ")
        print()
print(tables2(5))
