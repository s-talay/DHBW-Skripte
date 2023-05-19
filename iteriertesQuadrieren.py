def iteriertesQuad(basis,exp,mod):
    if(exp == 0):
        return 1
    if(exp%2 == 0):
        result = iteriertesQuad(basis,exp/2,mod)
        return (result*result)%mod
    else:
        result = iteriertesQuad(basis,exp-1,mod)
        return (basis*result)%mod
    
print(iteriertesQuad(2,182734123,977))