import numpy as np

datos=np.loadtxt("./grid.dat")



prod_long=1
prod_ant_diag_1=1
prod_diag_1=1
prod_ant_diag_2=1
prod_diag_2=1
i_prime=0
j_prime=0

for i in range(0,len(datos[0,:])-5):
    for j in range(0,len(datos[:,0])-5):
        prod_ant_long_1=1
        prod_ant_long_2=1
        for k in range(0,4):
            prod_ant_long_1=prod_ant_long_1*datos[i,j+k]
            prod_ant_long_2=prod_ant_long_2*datos[i+k,j]

        if(prod_ant_long_1<prod_ant_long_2):
            if(prod_ant_long_2>prod_long):
                prod_long=prod_ant_long_2
                i_prime=i
                j_prime=j
        if(prod_ant_long_1>prod_ant_long_2):
            if(prod_ant_long_1>prod_long):
                prod_long=prod_ant_long_2
                i_prime=i
                j_prime=j

print prod_long
print i_prime
print j_prime