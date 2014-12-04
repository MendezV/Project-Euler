import numpy as np

n=600851475143
datos = np.loadtxt("./lista_primos.dat")

for i in datos:
    a=n%i
    if(a==0):
        print i