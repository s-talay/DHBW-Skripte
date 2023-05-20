def f(s,n):
    m = int(n**0.5)
    return (s+m)**2 -n
def Sieb(B,C):
    for i in range (-C,C+1):
        val = f(i,B)
        print(i,": ",val)

Sieb(11111,10)