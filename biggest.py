#!/usr/bin/env python

def biggest(l):
    n = len(l)
    a = []
    for i in l:
        a.append(i)
    a.sort()
    print(a)
    print("largest number is: ",a[-1])
        
biggest([23,1,4,50,6])
