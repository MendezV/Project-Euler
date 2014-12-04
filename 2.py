
f_prev=0
f_curr=1
f_new=0
s=0
while (f_new<4000000):
    f_new= f_curr+f_prev
    if (f_new%2 == 0):
        s+=f_new
    f_prev=f_curr
    f_curr=f_new

print s