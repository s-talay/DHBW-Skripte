import hashlib

def mgf1(seed: bytes, length: int, hash_func=hashlib.sha256) -> bytes:
    hLen = hash_func().digest_size
    # https://www.ietf.org/rfc/rfc2437.txt
    # 1.If l > 2^32(hLen), output "mask too long" and stop.
    if length > (hLen << 32):
        raise ValueError("mask too long")
    # 2.Let T  be the empty octet string.
    T = b""
    # 3.For counter from 0 to \lceil{l / hLen}\rceil-1, do the following:
    # Note: \lceil{l / hLen}\rceil-1 is the number of iterations needed,
    #       but it's easier to check if we have reached the desired length.
    counter = 0
    while len(T) < length:
        # a.Convert counter to an octet string C of length 4 with the primitive I2OSP: C = I2OSP (counter, 4)
        C = int.to_bytes(counter, 4, 'big')
        # b.Concatenate the hash of the seed Z and C to the octet string T: T = T || Hash (Z || C)
        T += hash_func(seed + C).digest()
        counter += 1
    # 4.Output the leading l octets of T as the octet string mask.
    return T[:length]


def OAEP(seed: int, nachricht: int):
    if (byte_länge(seed) != 8):
        raise ValueError("Seed muss 8 Byte lang sein")

def Datenblock(nachricht: int):
    return 1<<nachricht.bit_length() | nachricht


def byte_länge(i):
    return (i.bit_length() + 7) // 8

def bytes_zu_int(i, endian = 'big'):
    return int.from_bytes(i,endian)

samen = 0xaa1122fe0815beef
nachricht = 0x466f6f62617220313233343536373839
samen_länge = 8
datenblock_länge = 128 -samen_länge -1

mgf_bytes = mgf1(samen.to_bytes(byte_länge(samen),'big'),datenblock_länge)
maskierter_datenblock = bytes_zu_int(mgf_bytes) ^ Datenblock(nachricht)
######################################

# print(maskierter_datenblock.to_bytes(byte_länge(maskierter_datenblock),'big'))
print(hex(maskierter_datenblock))

a = 0xea600669f6f16b3a2ad05d4b6d9b23911c8cc432fddd8d34a68d88af3d787b7eebf6cd1b720812086758ce56e24ab819ccd8fb5eedb1cae9f6f895667d7f89d0454b828777ecabc040a649c8956e78ec1c721370663065cbc343deabad9eb6f2aceab6bfed5bebe543aa3672cddf915c5b564848f4e6ec
b = 0xea600669f6f16b3a2ad05d4b6d9b23911c8cc432fddd8d34a68d88af3d787b7eebf6cd1b720812086758ce56e24ab819ccd8fb5eedb1cae9f6f895667d7f89d0454b828777ecabc040a649c8956e78ec1c721370663065cbc343deabad9eb6f2aceab6bfed5bea6543aa3672cddf915c5b564848f4e6ec
assert a == b
# assert maskierter_datenblock == 0xea600669f6f16b3a2ad05d4b6d9b23911c8cc432fddd8d34a68d88af3d787b7eebf6cd1b720812086758ce56e24ab819ccd8fb5eedb1cae9f6f895667d7f89d0454b828777ecabc040a649c8956e78ec1c721370663065cbc343deabad9eb6f2aceab6bfed5bea6543aa3672cddf915c5b564848f4e6ec
print(mgf1(maskierter_datenblock.to_bytes(119, 'big'), samen_länge).hex())

mgf = mgf1(maskierter_datenblock.to_bytes(byte_länge(maskierter_datenblock),'big'),samen_länge)
print(mgf.hex())
# maske_für_samen = int(mgf.hex(),16)
# # assert maske_für_samen == 0x713162084a4e0e6d

# maskierter_samen = samen ^ maske_für_samen

# print(mgf_bytes.hex()) # Maske fpr Datenblock DB
# print(hex(maskierter_datenblock)) # Maskierter Datenblock
# print(hex(maske_für_samen))
# print(hex(maskierter_samen))
