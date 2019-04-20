# import math
# def mode(n):
#     l = []
#     n.sort()
#     for i in n:
#         if i:
#             l.append(on.count(i))
#         return l


def mode(List):
    counter = 0
    num = List[0]
    for i in List:
        curr_frequency = List.count(i)
        if(curr_frequency > counter):
            counter = curr_frequency
            num = i
    return num


print(mode([2, 2, 2, 3, 3, 1, 1, 1, 1]))
