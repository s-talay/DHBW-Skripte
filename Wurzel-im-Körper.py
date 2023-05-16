def wurzelInKörper(a,p):
    if not ist_prim(p):
        raise ValueError("p ist keine Primzahl!")
    if(p+1)%4 == 0:
        w1 = a**((p+1)/4)
        w2 = (w1)%p
        return (w1,w2)
    else:
        t = (p-1)/2
        l = 0
        while t%2 == 0:
            t /=2
            l+=1
        
        raise ValueError("Nicht durch 4 teilbar, kein Bock das zu coden")



def ist_prim(n):
    if(n<2):
        return False
    for i in range(2, int(n**0.5)): # 2 bis Wurzel n
        if n%i == 0:
            return False
    return True