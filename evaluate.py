#!/usr/bin/env python

def evaluate(s):

    list1 = []
    for i in s:
        if i.isdigit():
            list1.append(i)
        else:
            a = int(list1.pop())
            b = int(list1.pop())
            if i == '+':
                ans = a + b
                list1.append(ans)
            elif i == '-':
                ans = a - b
                list1.append(ans)
            elif i == '*':
                ans = a * b
                list1.append(ans)
            elif i == '/':
                ans = a / b
                list1.append(ans)
    return (list1.pop())


print(evaluate("23+5"))
