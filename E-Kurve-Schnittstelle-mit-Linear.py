def Q_mod(r1,s1,r2,s2,mod):
    m = (s2-s1)/(r2-r1)
    if(isinstance(m,float)):
        nenner = inversesImMod((r2-r1),mod)
        m = (s2-s1)*nenner
    r3 = m**2-r1-r2
    s3 = m**3-2*m*r1-m*r2+s1
    return (r3%mod,s3%mod)

def Q_tan_mod(r,s,a,mod):
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



mod = 787
a = 3

x1 = 279
y1 = 183

x2 = 422
y2 = 287

x3 = 651
y3 = 528

L1 = Q_mod(x1,y1,x2,y2,mod)
L2 = Q_mod(x1,y1,x3,y3,mod)

T2 = Q_tan_mod(x2,y2,a,mod)
T3 = Q_tan_mod(x3,y3,a,mod)

print("L1: ",L1)
print("L2: ",L2)
print("T2: ",T2)
print("T3: ",T3)