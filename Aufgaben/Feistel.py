def feistel_function(InR,K):
    B1 = InR & 0x000F 
    B2 = (InR & 0x00F0)>> 4
    B3 = (InR & 0x0F00)>> 8
    B4 = (InR & 0xF000)>> 12

    b1 = flip_ordnung(B4)
    b4 = flip_ordnung(B1)
    b2 = s_box(B2)
    b3 = s_box(B3)

    b = (b4<<12)|(b3<<8)|(b2<<4)|(b1<<0)

    return b ^ K

def feistel_round(I,K):
    InL = I>>16
    InR = I & 0x0000FFFF
    OutR = InL ^ feistel_function(InR,K)
    OutL = InR
    return (OutL<<16)|OutR

def feistel_round_rev(I,K):
    InL = I>>16
    InR = I & 0x0000FFFF
    OutL = InR ^ feistel_function(InL,K)
    OutR = InL
    return (OutL<<16)|OutR

def flip_ordnung(b):
    b1 = (b & 0b1000)>>3
    b2 = (b & 0b0100)>>1
    b3 = (b & 0b0010)<<1
    b4 = (b & 0b0001)<<3
    return (b1|b2|b3|b4)

def s_box(b):
    liste = [
        0x4,0x3,0x9,0xa,0xb,0x2,0xe,0x1,
        0xd,0xc,0x8,0x6,0x7,0x5,0x0,0xf        
        ]
    return liste[b]

def enc(P):
    k1 = 0x1aa2
    k2 = 0x2bb3
    k3 = 0x3cc4
    r1 = feistel_round(P,k1)
    r2 = feistel_round(r1,k2)
    r3 = feistel_round(r2,k3)
    return r3

def dec(C):
    k1 = 0x1aa2
    k2 = 0x2bb3
    k3 = 0x3cc4
    r1 = feistel_round_rev(C,k3)
    r2 = feistel_round_rev(r1,k2)
    r3 = feistel_round_rev(r2,k1)
    return r3

P1 = 0x12345678
C1 = enc(P1)
print(hex(C1))
PP = dec(C1)
print(hex(PP))

print("==============")

P = 0xabcd0815
print(hex(enc(P)))
C = 0x12345678
print(hex(dec(C)))

