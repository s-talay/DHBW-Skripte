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
a = 7
m = 7
a_inv = inversesImMod(a, m)

print("Inverse von {} im Körper mit dem Modulus {}: {}".format(a, m, a_inv))
