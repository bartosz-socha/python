import sys
import math
import timeit

print(math.pow(2, 32) - 1)
atuple1 = (6, 4, 5)
atuple2 = 6, 4, 5
atuple3 = 6,
atuple4 = 5000000000
alist = ["awans", 4, True]
a, b, c = alist
atuple5 = tuple(alist)
d, e, f = atuple5
astring1 = str(atuple5)
astring2 = str(alist)

print(type(atuple1))
print(type(atuple2))
print(type(atuple3))
print(type(atuple4))
print(alist[0])
print(atuple5[0])
print(astring1[2])
print(astring2[2])
print(a)
print(f)
print(sys.getsizeof(atuple5))
print(sys.getsizeof(alist), "bytes")
print(sys.getsizeof(atuple4), "bytes")
print(type(atuple4))
