def gcd(a,b):
    if b==0:
        return a
    r=a%b
    d=gcd(b,r)
    return d
GCD=gcd(28,42)
print("gcd", GCD)