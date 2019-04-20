#!/usr/bin/env python

def median(list1):
    list1.sort()
    n = (len(list1) - 1)
    a = int((n + 1)/2)
    b = list1[a]
    return b

print(median([1,2,4,3,4,6,4]))
