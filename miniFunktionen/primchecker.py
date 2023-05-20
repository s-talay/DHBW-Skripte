def ist_prim(n):
    if(n<2):
        return False
    for i in range(2, int(n**0.5)): # 2 bis Wurzel n
        if n%i == 0:
            return False
    return True