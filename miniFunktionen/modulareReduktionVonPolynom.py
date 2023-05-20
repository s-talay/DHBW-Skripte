def get_msb_exp(n):
    i = 0
    while(True):
        if(n == 1):
            return i
        n = n>>1
        i+=1
def reduziert(n,rel):
    rel_exp = get_msb_exp(rel)
    num = n
    while(True):
        exp = get_msb_exp(num)
        if(exp>=rel_exp):
            num = num ^ (rel<<(exp-rel_exp))
        else:
            return num

num = 0x100001
relation = 0x1053
print("resultat: ",hex(reduziert(num,relation)))
