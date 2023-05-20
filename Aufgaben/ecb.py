def getC(p):
    dict = {
        0x11b2e5ee:0x48657920,
        0x1ed9df8b:0x714d4302,
        0x2bd4da90:0x714d4300,
        0x48657920:0xe9e6c104,
        0x51a08949:0xb2608c8f,
        0x51a50d5c:0x51a08949,
        0x68657921:0xf5eff3de,
        0x714d4300:0x5fab4208,
        0x714d4301:0x4100f7ec,
        0x714d4302:0x4848118a,
        0x716de7c1:0x714d4301,
        0x845f66f0:0x68657921,
        0xc202e091:0xa8d1c397,
        0xcd65575e:0xc202e091,
        0xd6c4fe4e:0xfa05f5af,
        0xfa05f5af:0xaa6799b0
    }
    return dict[p]

def getP(c):
    dict = {
        0x48657920:0x11b2e5ee,
        0x714d4302:0x1ed9df8b,
        0x714d4300:0x2bd4da90,
        0xe9e6c104:0x48657920,
        0xb2608c8f:0x51a08949,
        0x51a08949:0x51a50d5c,
        0xf5eff3de:0x68657921,
        0x5fab4208:0x714d4300,
        0x4100f7ec:0x714d4301,
        0x4848118a:0x714d4302,
        0x714d4301:0x716de7c1,
        0x68657921:0x845f66f0,
        0xa8d1c397:0xc202e091,
        0xc202e091:0xcd65575e,
        0xfa05f5af:0xd6c4fe4e,
        0xaa6799b0:0xfa05f5af
    }
    return dict[c]

iv = 0x19c5f069
p1 = 0x48657920
c1 = getC(p1 ^ iv)
p2 = 0x48657920
c2 = getC(p2 ^ c1)
p3 = 0x68657921
c3 = getC(p3 ^ c2)
print("c1: ",hex(c1))
print("c2: ",hex(c2))
print("c3: ",hex(c3))

print("")

ctr = 0x0
nonce_base = 0x714d4300
def enc_ctr(p):
    global ctr
    nonce = nonce_base+ctr
    ctr+=1
    return getC(nonce)^p


p1 = 0x48657920
c1 = enc_ctr(p1)
p2 = 0x48657920
c2 = enc_ctr(p2)
p3 = 0x68657921
c3 = enc_ctr(p3)

print("c1: ",hex(c1))
print("c2: ",hex(c2))
print("c3: ",hex(c3))

