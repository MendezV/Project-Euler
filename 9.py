import math
import numpy as np

prod=0
for a in range (1,1000):
    for b in range (1,1000):
        c=np.sqrt(a**2+b**2)
        if((c-math.floor(c))==0):
            if(a+b+c==1000):
                if(prod==0):
                    prod=a*b*c
                    print prod
                    print a,b,c
