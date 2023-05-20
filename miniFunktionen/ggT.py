def ggT(a,b):
    while b:
        a,b = b, a%b
    return a

n = 11111
x = (2*5**2*11*13)%n
y = (106*107*111)%n
a = x-y
print(ggT(x-y,n))

