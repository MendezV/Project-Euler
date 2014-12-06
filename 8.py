import numpy as np
prod_new=1
prod=1
count=0
datos=np.loadtxt("./1000digitnum.dat")
for i in range (0,987):
    for j in range (0,13):
        prod_new= prod_new*datos[i+j]
    if(prod_new>prod):
        prod=prod_new
        count=i
    prod_new=1
print count
print prod