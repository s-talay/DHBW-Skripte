primlist = []

def ist_prim(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def finde_primezahlen(n):
    primes = []
    if n < 2:
        return primes
    try:
        with open('primes.txt', 'r') as f:
            for line in f:
                primes.append(int(line.strip()))
    except FileNotFoundError:
        pass  # File doesn't exist yet
    start = primes[-1] + 1 if primes else 2
    for i in range(start, n+1):
        if ist_prim(n):
            primes.append(i)
    
    # Save updated list of primes to file
    with open('primes.txt', 'w') as f:
        for p in primes:
            f.write(str(p) + '\n')
    
    return primes

def liste_prim_potenzen(n):
    list = []
    for i in range(2, n):
        return
finde_primezahlen(999999999999)