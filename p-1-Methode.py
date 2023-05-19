
def ist_prim(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def ggT(a,b):
    while b:
        a,b = b, a%b
    return a

def findeFaktor(n):
    a = 2
    exp = 2
    while(n%2 == 0):
        return 2
    while(True):
        g = ggT(a**exp - 1,n)
        if(g > 1):
            print("Faktor gefunden: ",g)
            return g
        exp+=1

def pMinus1(n):
    faktoren = []
    numb = n
    while(True):
        faktor = findeFaktor(numb)
        faktoren.append(faktor)
        numb = int(numb/faktor)
        print("numb: ",numb)
        print("faktor: ",faktor)
        if(numb == 1):
            return faktoren

print(pMinus1(12345678987654321))