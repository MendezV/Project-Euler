import numpy as np

datos=np.loadtxt("./grid.dat")



prod=1
prod_diag_1=1
prod_ant_diag_2=1
prod_diag_2=1
i_prime=0
j_prime=0
pos=0
i_max=len(datos[:,0])-1
j_max=len(datos[0,:])-1
for i in range(0,i_max-3):
    for j in range(0,j_max-3):
        prod_ant_long_1=1
        prod_ant_long_2=1
        prod_ant_diag_1=1
        for k in range(0,4):
            prod_ant_long_1=prod_ant_long_1*datos[i,j+k]
            prod_ant_long_2=prod_ant_long_2*datos[i+k,j]
            prod_ant_diag_1=prod_ant_diag_1*datos[i+k,j+k]

        if(prod_ant_long_1<prod_ant_long_2)&(prod_ant_diag_1<prod_ant_long_2):
            if(prod_ant_long_2>prod):
                prod=prod_ant_long_2
                i_prime=i
                j_prime=j
                pos=datos[i,j]
        if(prod_ant_long_1>prod_ant_long_2)&(prod_ant_diag_1<prod_ant_long_1):
            if(prod_ant_long_1>prod):
                prod=prod_ant_long_1
                i_prime=i
                j_prime=j
                pos=datos[i,j]
        if(prod_ant_long_1<prod_ant_diag_1)&(prod_ant_diag_1>prod_ant_long_2):
            if(prod_ant_diag_1>prod):
                prod=prod_ant_diag_1
                i_prime=i
                j_prime=j
                pos=datos[i,j]

print prod
print i_prime
print j_prime
print pos