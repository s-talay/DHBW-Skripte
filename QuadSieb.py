def f(s,n):
    m = int(n**0.5)
    return (s+m)**2 -n
for i in range (-10,11):
    val = f(i,11111)
    print(i,": ",val)