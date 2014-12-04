import numpy as np

s=0

for i in range (0,1000):
    a=i%3
    b=i%5
    if (b==0) | (a==0):
        s+=i
print s

