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