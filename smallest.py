#!/usr/bin/env python

def smallest(list1):
    minimum = list1[0]
    for i in list1:
        if i < minimum:
            minimum = i
    return minimum
         


print(smallest([12,1,34,23]))
