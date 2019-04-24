e = int(input("Enter the number from: "))
e1 = int(input("To: "))
div = int(input("Enter a number to divide: "))
mult = int(input("Not multiple of: "))

l = []
for i in range(e, e1):
    if i % div == 0 and i % mult != 0:
        l.append(str(i))
print( ','.join(l))
