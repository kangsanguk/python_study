from math import pi
from random import random

def getarea(r):
    area = round(pi * pow(r, 2), 2)
    return area

r = round(random()*10, 2)
print("원의 반지름:", r)
print("원주율 pi: %.4f" %pi)
area = getarea(r)
print("반지름 " +str(r) + "인 원의 면적은 " + str(area))

