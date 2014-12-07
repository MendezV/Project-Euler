import numpy as np

datos= np.loadtxt("./primos_menores_a_2000000.dat")

s=0
for i in datos:
    s+=i
print s