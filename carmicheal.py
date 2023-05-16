
def carmicheal(n):
    for a in range(2, n):
        if ggT(a, n) == 1:
            if pow(a, n-1, n) != 1:
                return False
    return True

def ggT(a, b):
    while b:
        a, b = b, a % b
    return a

m=275237
k=5354228880
a = ggT(2**k - 1,m)
print(a)