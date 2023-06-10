R = 1
S = 3


modulus = 17
B = 5
A = 3

def erweiterterEuklid(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        ggT, x, y = erweiterterEuklid(b % a, a)
        return (ggT, y - (b // a) * x, x)
def inversesImMod(a, m=modulus):
    ggT, x, _ = erweiterterEuklid(a, m)
    if ggT != 1:
        raise ValueError("Die Zahlen sind nicht teilferfremd")
    else:
        return x % m
def m(r=R,s=S,a=A,mod=modulus):
    m = (3*r**2+3)/(2*s)
    if isinstance(m,float):
        m = (3*r**2+3)*inversesImMod(2*s)
    return int(m)%mod
M = m()
def u(m=M,r=R,mod=modulus):
    return (m**2-2*r)%mod
U = u()
def v(m=M,u=U,r=R,s=S,mod=modulus):
    return(m*(u-r)+s)%mod
V = v()

print("m: ",M)
print("u: ",U)
print("v: ",V)







def F(x,y,a=A,b=B,mod=modulus):
    return (y**2-x**3-a*x-b)%mod
def pF(x,y,a=A,b=B,mod=modulus):
    print(F(x,y,a,b,mod))