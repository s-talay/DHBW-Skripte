def ggT(a,b):
    while b:
        a,b = b, a%b
    return a

a = 1363
b = 899
print(ggT(a,b))

