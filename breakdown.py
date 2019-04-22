def breakdown(n):
    formatter = "{} X {} = {}({} left)"
    l = [1000, 500, 100, 20, 1]
    for i in l:
        count = int(n/i)
        n -= count*i
        print(formatter.format(i, count, i*count, n))

n = int(input("Enter the number to breakdown: "))
print(breakdown(n))
