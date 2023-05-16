def ka(inval):
    outval = ((inval & 0xe0) >> 4) | ((inval & 0x1c) << 3) | ((inval & 0x02) >> 1) | ((inval & 0x01) << 4)
    return outval

for i in range(0,0x100):
    print(hex(i)," : ",hex(ka(i)))
# for i in range(0,0x100):
#     print(i," : ",ka(i))
# for i in range(0,0x100):
#     print(bin(i)," : ",bin(ka(i)))