def wurzelInKörper(a,p):
    if(p+1)%4 == 0:
        w1 = a**((p+1)/4)
        w2 = (w1)%p
        return (w1,w2)
    else:
        raise ValueError("Nicht durch 4 teilbar, kein Bock das zu coden")
