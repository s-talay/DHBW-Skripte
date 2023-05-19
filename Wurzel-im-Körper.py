def ist_prim(n):
    if(n<2):
        return False
    for i in range(2, int(n**0.5)): # 2 bis Wurzel n
        if n%i == 0:
            return False
    return True

def iteriertesQuad(basis,exp,mod):
    if(exp == 0):
        return 1
    if(exp%2 == 0):
        result = iteriertesQuad(basis,exp/2,mod)
        return (result*result)%mod
    else:
        result = iteriertesQuad(basis,exp-1,mod)
        return (basis*result)%mod

def wurzelInKörper(a,p):
    if not ist_prim(p):
        raise ValueError("p ist keine Primzahl!")
    if(iteriertesQuad(a,(p-1)/2,p) != 1):
        raise ValueError("a ist kein Quadrat")
    if(p+1)%4 == 0:
        w1 = a**((p+1)/4)
        w2 = (-w1)%p
        return (w1,w2)
    else:
        #
        t = (p-1)/2
        l = 0
        while t%2 == 0:
            t /=2
            l+=1
        print("l = ",l)
        print("t = ",t)
        b = 0
        while (iteriertesQuad(b,(p-1)/2,p) != 976):
            b+=1
            if(b == 977):
                raise IndexError("Keine Ahnung Bro")
        print("b = ",b)
        n=0
        for i in range(0,l):
            print(i)
            exp = 2**(l-(i+1))*t
            print("exp = ",exp)
            c = iteriertesQuad(a,(2**(l-(i+1))*t),p) * b**n
            print("c = ",c)
            if(c == 1):
                n = n/2
            else:
                n = n/2 + (p-1)/4
            print("n = ",n)

        print("final a = ",a)
        print("final t = ",t)
        print("final b = ",b)
        print("final p = ",p)   
        w1 = (iteriertesQuad(a,(t+1)/2,p) * b**n)%p
        w2 = (-w1) % p
        return (w1,w2)


print(wurzelInKörper(269,977))
print(269**31.0 %977)