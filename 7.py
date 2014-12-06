import numpy as np
datos = np.loadtxt("./lista_primos.dat")

for i in range (104729,105000):
    count=0
    for j in datos:
        if(i%j!=0):
            count +=1
        if(count==10000):
            print i
            