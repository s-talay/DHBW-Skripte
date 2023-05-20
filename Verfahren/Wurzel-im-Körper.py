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
        return("p ist keine Primzahl!")
    if(iteriertesQuad(a,int((p-1)/2),p) != 1):
        return("a ist kein Quadrat")
    if(p+1)%4 == 0:
        w1 = a**(int((p+1)/4))
        w2 = (-w1)%p
        return (w1,w2)
    else:
        t = int((p-1)/2)
        l = 0
        while t%2 == 0:
            t = int(t/2)
            l+=1
        b = 0
        while (iteriertesQuad(b,int((p-1)/2),p) != 976):
            b+=1
            if(b == 977):
                return("Keine Ahnung Bro")
        n=0
        for i in range(0,l):
            exp = 2**(l-(i+1))*t
            c = iteriertesQuad(a,(2**(l-(i+1))*t),p) * b**n
            if(c == 1):
                n = int(n/2)
            else:
                n = int(n/2 + (p-1)/4)
        w1 = (iteriertesQuad(a,int((t+1)/2),p) * b**n)%p
        w2 = (-w1) % p
        return (w1,w2)
    
def f(x):
    return (x**3 + 7*x + 17)%977

def F(x,y):
    return (y**2-f(x))%977

w100, q100 = wurzelInKörper(f(100),977)
print("Wurzel:",w100,",",q100)
print("Prüfen: ",F(100,w100))

w400,q400 = wurzelInKörper(f(400),977)
print("Wurzel:",w400,",",q400)
print("Prüfen: ",F(400,w400))

w500,q500 = wurzelInKörper(f(500),977)
print("Wurzel:",w500,",",q500)
print("Prüfen: ",F(500,w500))

print(" ")
print(" ")
print(" ")
print(wurzelInKörper(269,977))
print(wurzelInKörper(764,977))
print(wurzelInKörper(524,977))
print(wurzelInKörper(275,977))
print(wurzelInKörper(734,977))