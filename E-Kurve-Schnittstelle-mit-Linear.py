def Q(r1,s1,r2,s2,mod):
    m = (s2-s1)/(r2-r1)
    if(isinstance(m,float)):
        nenner = inversesImMod((r2-r1),mod)
        m = (s2-s1)*nenner
    r3 = m**2-r1-r2
    s3 = m**3-2*m*r1-m*r2+s1
    return (r3%mod,s3%mod)
def Q_tan(r,s,a,mod):
    m = (3*r**2 + a)/(2*s)
    if(isinstance(m,float)):
        nenner = inversesImMod((2*s)%mod,mod)
        m = (3*r**2 + a)*nenner
    u = m**2 - 2*r
    v = m*(u - r) + s
    return (u%mod,v%mod)

def Q(r1,s1,r2,s2):
    m = (s2-s1)/(r1-r1)
    r3 = m**2-r1-r2
    s3 = m**3-2*m*r1-m*r2+s1
    return (r3,s3)
def Q_tan(r,s,a):
    m = (3*r**2 + a)/(2*s)
    u = m**2 - 2*r
    v = m*(u - r) + s
    return (u,v)



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


r = 7
s = 5
a = 7
mod = 19
Q11,Q12 = Q_tan(r,s,a,mod)
Q21,Q22 = Q_tan(Q11,Q12,a,mod)
Q31,Q32 = Q_tan(Q21,Q22,a,mod)

print(Q31,Q32)
print(15%None)