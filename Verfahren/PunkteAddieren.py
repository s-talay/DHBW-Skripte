# NOT CORRECT

def Q_mod_inChar2(r1,s1,r2,s2,a,mod):
    m = (s2+s1)/(r2+r1)
    if(isinstance(m,float)):
        nenner = inversesImMod((r2+r1),mod)
        m = (s2+s1)*nenner
    u = m**2 + m + a + r1 +r2
    v = m * (r1 + u) + u + s1
    return (u%mod,v%mod)

def Q_tan_mod_inChar2(r,s,a,mod):
    m = r + s/r
    if(isinstance(m,float)):
        nenner = inversesImMod((r)%mod,mod)
        m = r + s*nenner
    print("m: ",m%mod)
    u = m**2 + m + a
    v = m*(r + u) + u + s
    return (u%mod,v%mod)


def erweiterterEuklid(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        ggT, x, y = erweiterterEuklid(b % a, a)
        return (ggT, y - (b // a) * x, x)

def inversesImMod(a, mod):
    ggT, x, _ = erweiterterEuklid(a, mod)
    if ggT != 1:
        raise ValueError("Die Zahlen sind nicht teilferfremd")
    else:
        return x % mod