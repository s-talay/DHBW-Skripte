import hashlib

def iteriertesQuad(basis,exp,mod):
    if(exp == 0):
        return 1
    if(exp%2 == 0):
        result = iteriertesQuad(basis,exp/2,mod)
        return (result*result)%mod
    else:
        result = iteriertesQuad(basis,exp-1,mod)
        return (basis*result)%mod


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


def Datenblock(nachricht: int):
    return 1<<nachricht.bit_length()+1 | nachricht


def byte_länge(i):
    return (i.bit_length() + 7) // 8

def bytes_zu_int(i, endian = 'big'):
    return int.from_bytes(i,endian)


e_test = 0x10001
n_test = 0xAF5466C26A6B662AC98C06023501C9DF6036B065BD1F6804B1FC86307718DA4048211FD68A06917DE6F81DC018DCAF84B38AB77A6538BA2FE6664D3FB81E4A0886BBCDAB071AD6823FE20DF1CD67D33FB6CC5DA519F69B11F3D48534074A83F03A5A9545427720A30A27432E94970155A026572E358072023061AF65A2A18E85
samen_test = 0xaa1122fe0815beef
nachricht_test = 0x466f6f62617220313233343536373839
samen_länge = 8
modul_länge = 128
datenblock_länge = modul_länge -samen_länge -1

am_testen = True
am_drucken = True

def OAEP(samen: int, nachricht: int) -> bytes:
    if (byte_länge(samen) != 8):
        raise ValueError("Seed muss 8 Byte lang sein")
    
    maske_für_datenblock = bytes_zu_int(mgf1(samen.to_bytes(byte_länge(samen),'big'),datenblock_länge))
    if am_testen:
        assert maske_für_datenblock == 0xea600669f6f16b3a2ad05d4b6d9b23911c8cc432fddd8d34a68d88af3d787b7eebf6cd1b720812086758ce56e24ab819ccd8fb5eedb1cae9f6f895667d7f89d0454b828777ecabc040a649c8956e78ec1c721370663065cbc343deabad9eb6f2aceab6bfed5beb232cc55413bfffa06e68627d7ec3ded5 
    if am_drucken:
        print(hex(maske_für_datenblock))
    
    maskierter_datenblock = (maske_für_datenblock) ^ Datenblock(nachricht)
    if am_testen:
        assert maskierter_datenblock == 0xea600669f6f16b3a2ad05d4b6d9b23911c8cc432fddd8d34a68d88af3d787b7eebf6cd1b720812086758ce56e24ab819ccd8fb5eedb1cae9f6f895667d7f89d0454b828777ecabc040a649c8956e78ec1c721370663065cbc343deabad9eb6f2aceab6bfed5bea6543aa3672cddf915c5b564848f4e6ec 
    if am_drucken:
        print(hex(maskierter_datenblock))

    mgf_bytes2 = mgf1(maskierter_datenblock.to_bytes(byte_länge(maskierter_datenblock),'big'),samen_länge)
    maske_für_samen = bytes_zu_int(mgf_bytes2)
    if am_testen:
        assert maske_für_samen ==  0x713162084a4e0e6d
    if am_drucken:
        print(hex(maske_für_samen))

    maskierter_samen = samen ^ maske_für_samen
    if am_testen:
        assert maskierter_samen ==  0xdb2040f6425bb082
    if am_drucken:
        print(hex(maskierter_samen))

    enkodierte_nachricht = (maskierter_samen << maskierter_datenblock.bit_length()) | maskierter_datenblock
    if am_testen:
        assert enkodierte_nachricht ==  0x00db2040f6425bb082ea600669f6f16b3a2ad05d4b6d9b23911c8cc432fddd8d34a68d88af3d787b7eebf6cd1b720812086758ce56e24ab819ccd8fb5eedb1cae9f6f895667d7f89d0454b828777ecabc040a649c8956e78ec1c721370663065cbc343deabad9eb6f2aceab6bfed5bea6543aa3672cddf915c5b564848f4e6ec
    if am_drucken:
        print(hex(enkodierte_nachricht))

    enkodierte_nachricht_bytes = b'\x00' + enkodierte_nachricht.to_bytes(byte_länge(enkodierte_nachricht),'big')

    return enkodierte_nachricht_bytes

def dekodiertes_OAEP(enkodierte_nachricht: int, e: int, n: int) -> int:
    dekodierte_nachricht = iteriertesQuad(enkodierte_nachricht,e_test,n_test)
    if am_testen:
        assert dekodierte_nachricht == 0x1b57819fa11340ac8b1843c87db7adb126daa8b6dde1feefd7af721cee8f46b6e2c361fc04ac055406a342187388b019dba0bc3f6503f267b848f7cc86b29a3d0b32730ccf04c5a8a3e1255708cbc6a6a648015e30f38b1c1c7aa9d2b0e67a775c7ad1cb72ff76c000af46e7cada3c3b45b5f4d1ec8e0596928cc9b46ee2b53d
    if am_drucken:
        print(hex(dekodierte_nachricht))
        
    dekodierte_nachricht_bytes = b'\x00' + dekodierte_nachricht.to_bytes(byte_länge(dekodierte_nachricht),'big')
    return dekodierte_nachricht_bytes


kodierte_nachricht_bytes_test = OAEP(samen_test,nachricht_test)
print(kodierte_nachricht_bytes_test)
print(dekodiertes_OAEP(bytes_zu_int(kodierte_nachricht_bytes_test),e_test,n_test))