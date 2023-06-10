import base64
import binascii

# openssl ecparam -name secp256r1 -param_enc explicit -text -noout
p = 0x00ffffffff00000001000000000000000000000000ffffffffffffffffffffffff
a = 0x00ffffffff00000001000000000000000000000000fffffffffffffffffffffffc
b = 0x5ac635d8aa3a93e7b3ebbd55769886bc651d06b0cc53b0f63bce3c3e27d2604b
G = 0x046b17d1f2e12c4247f8bce6e563a440f277037d812deb33a0f4a13945d898c2964fe342e2fe1a7f9b8ee7eb4a7c0f9e162bce33576b315ececbb6406837bf51f5
r_G = 0x6b17d1f2e12c4247f8bce6e563a440f277037d812deb33a0f4a13945d898c296
s_G = 0x4fe342e2fe1a7f9b8ee7eb4a7c0f9e162bce33576b315ececbb6406837bf51f5
n = 0x00ffffffff00000000ffffffffffffffffbce6faada7179e84f3b9cac2fc632551
h = 0x01

# openssl.exe asn1parse -in pub_key.pem --dump
# 00 04 ignorieren und erste hälfte als r und zweite hälfte als s nehmen
r = 0x8c3aa86d54441a69d3a30c788e5674844ab298253b92f1673e2de534ee98f79d
s = 0x511ef4818b008be75c727ca3dde25c98281b75cea75b6969bd83ebae3e3518f6

# cat signatur.der | xxd -r -ps | openssl.exe asn1parse -inform DER --dump
# erster int ist r 
# zweiter int ist s
#   Laut RFC3279:
#   Dss-Sig-Value  ::=  SEQUENCE  {
#       r       INTEGER,
#       s       INTEGER  }
r_sig = 0x4854A53830FAB30CAC49C91B72E7F84D8CB25102DB220F6DC7F1A8B31B29B913
s_sig = 0x86ABF01F3AFF9B2A0B3823F2581983A8C38264660EC66BB2F8C648BEE88D36E0

import hashlib
import sage

def Hash(message):
    sha256 = hashlib.sha256()
    sha256.update(message.encode('utf-8'))
    sha256_hex = sha256.hexdigest()
    return sha256_hex
def erweiterterEuklid(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        ggT, x, y = erweiterterEuklid(b % a, a)
        return (ggT, y - (b // a) * x, x)
def inversesImMod(a, m):
    ggT, x, _ = erweiterterEuklid(a, m)
    if ggT != 1:
        raise ValueError("Die Zahlen sind nicht teilferfremd")
    else:
        return x % m

m = "Kryptologie DHBW Mannheim"
e = Hash(m)
w = inversesImMod(s,n)
u1 = e*w % n
u2 = r*w % n