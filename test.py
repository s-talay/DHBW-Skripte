def test(inval):
    outval = ((inval & 0xe0) >> 4) | ((inval & 0x1c) << 3) | ((inval & 0x02) >> 1) | ((inval & 0x01) << 4)
    return outval