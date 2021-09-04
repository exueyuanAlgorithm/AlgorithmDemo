a = "abd"
b = set(a)
print(b)

a = 1
print(hash(a))
print(hash("abdcsfd"))
# print(hash([2, 3, 5]))


# class AAA:
#     def __init__(self):
#         self.a = 5
#
#
# a = AAA()
# b = hash(a)
# print(b)
print(bin(12))
print(bin(4))
print(bin(12 ^ 4))

a = "3"
b = a.split(".")
print(b)

import math
print(math.log2(10**9))

# print(2**30)
# print(bin(5))
from collections import deque
my_deque = deque()
print(len(my_deque))
if my_deque:
    print("a")

import heapq
my_list = []
b = (4, 9)
a = (3,8)
c = (2, 111)
heapq.heappush(my_list, a)
heapq.heappush(my_list, b)
heapq.heappush(my_list, c)
print(my_list)

a = set()
a.add(3)
a.remove(3)

a = [3, 8, 7, 3]
a.remove(3)
print(a)

print([item for item in range(31)])