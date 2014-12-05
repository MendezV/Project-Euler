def reverse(st):
    rev = ""
    for i in range(0 ,len(st)):
        rev += st[(len(st) -1) - i]
    return rev

pal=0
for i in range (100,999):
    for j in range (100,999):
        mult=i*j
        mult_str= str(mult)
        if (mult_str== reverse(mult_str)):
            if(mult>pal):
                pal = mult
print pal