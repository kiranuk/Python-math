import math
"""a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence."""
C = 50
H = 30
l = []
D = [x for x in input().split(',')]
for i in D:
    r = str(round(math.sqrt(2*C*float(i)/30)))
    l.append(r)
print(','.join(l))
