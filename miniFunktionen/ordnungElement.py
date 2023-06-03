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

for i in range(1,17):
    print(i," : ",ord(i,17))

