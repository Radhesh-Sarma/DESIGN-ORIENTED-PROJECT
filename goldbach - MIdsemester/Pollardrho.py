import random,math
import sympy
f = lambda x: x**2 +1
def pollardrhofactorization(n):
    if(n==1):
        return n
    if(n%2 == 0):
        return 2
    if(sympy.isprime(n)):
        return n    
    x = random.randrange(2,n)
    y = x
    c = random.randrange(1,n)
    d = 1
    while(d == 1):
        x = (f(x) + c + n) % n
        y = (f(y) + c + n) % n
        y = (f(y) + c + n) % n
        d = math.gcd(abs(x-y),n)
        if(d == n):
            return pollardrhofactorization(n)           
    return d        


    