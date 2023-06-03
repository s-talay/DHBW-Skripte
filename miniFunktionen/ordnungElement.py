def iteriertesQuad(basis,exp,mod):
    if(exp == 0):
        return 1
    if(exp%2 == 0):
        result = iteriertesQuad(basis,exp/2,mod)
        return (result*result)%mod
    else:
        result = iteriertesQuad(basis,exp-1,mod)
        return (basis*result)%mod

def ord(n,mod):
    for i in range(1,mod):
        if(iteriertesQuad(n,i,mod) == 1):
            return i
    raise ValueError("Kein Element")

def ggT(a,b):
    while b:
        a,b = b, a%b
    return a

def ist_primitives_element(n, mod):
    if ggT(n,mod) != 1:
        return False

    ord = 1
    while ord < mod-1:
        if iteriertesQuad(n,ord,mod) == 1:
            return False
        ord += 1
    return ord == mod-1

for i in range(1,17):
    print(i,":",ist_primitives_element(i,17))

