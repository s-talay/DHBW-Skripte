def iteriertesQuad(basis,exp,mod):
    if(exp == 0):
        return 1
    if(exp%2 == 0):
        result = iteriertesQuad(basis,exp/2,mod)
        return (result*result)%mod
    else:
        result = iteriertesQuad(basis,exp-1,mod)
        return (basis*result)%mod

def decrypt(n,d,cipher):
    return iteriertesQuad(cipher,d,n)

p = 2**206-5
q = 2**226-5
n = p*q
d = 0xaffe0815

c1 = 0x78766a52455329b486aaa414c3a029834a7e4b6ed87019dce4056f4d8999b137404d9ec4df28da201c9b0bc142deb1d86ff94d83becc
c2 = 0x670b865216dfd0aacd5f7fa8802e704fa82f3fb9c7dbe3eb5a9ec308a1a2288648b15d5cc8ba2f54b245a972aea977932c9c84cf6422
c3 = 0x61d5f2a4298bff3d6ebcd78830fb9181d97235623819eb7c60b92dcdf836a6cf731c60187e72f471c05d1c6eab216c3f6032af3c5370
c4 = 0x3651009d02a0c72b9bc206c57d12277594d9eaad28bb3de5d661670b42f1cfafe688b9674e34d4ad79db898205417086e7e1877b9ef1
c5 = 0x96e51d4675c6be5b14ec0cf2a9e9a9610a99d632723b3f1fcfc6b36806f5d74045f47622817cc35f6ffe9afe29f0aa236cbe12371651

m1 = decrypt(n,d,c1)
m2 = decrypt(n,d,c2)
m3 = decrypt(n,d,c3)
m4 = decrypt(n,d,c4)
m5 = decrypt(n,d,c5)
print("[",len(str(hex(m1))),", ",len(str(bin(m1))),", ",len(str(int(m1))),"]","c1: ",hex(m1))
print("[",len(str(hex(m2))),", ",len(str(bin(m2))),", ",len(str(int(m2))),"]","c2: ",hex(m2))
print("[",len(str(hex(m3))),", ",len(str(bin(m3))),", ",len(str(int(m3))),"]","c3: ",hex(m3))
print("[",len(str(hex(m4))),", ",len(str(bin(m4))),", ",len(str(int(m4))),"]","c4: ",hex(m4))
print("[",len(str(hex(m5))),", ",len(str(bin(m5))),", ",len(str(int(m5))),"]","c5: ",hex(m5))