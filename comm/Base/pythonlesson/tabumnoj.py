import random
from random import *

listt = []
for i in range(10):
    listt.append(randint(0,100))
listt.sort()
print(listt)
a = int(input())
i = 0
while(a >= listt[i]):
    i += 1
listt.insert(i,a)
print(listt)
