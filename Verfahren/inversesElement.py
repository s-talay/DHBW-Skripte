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
a = 548
m = 1151
print(inversesImMod(a, m))