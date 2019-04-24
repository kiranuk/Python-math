# To find out factorial of a number
def fact(n):
    if n == 0:
        return True
    return n * fact(n-1)


print(fact(10))
