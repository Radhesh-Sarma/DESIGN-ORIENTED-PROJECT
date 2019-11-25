import random, math, timeit

def gcd(a, b):
  while b:
    a, b = b, a%b
  return a

def f1(x,n):
  return (x*x-1)%n

def f2(x,n):
  return (x*x+1)%n
def f3(x,n):
  return (x*x*x-1)%n
def f4(x,n):
  return (4*x*x-2*x+41)%n
def f5(x,n): return (x+math.sqrt(n))%n
def f6(x,n): return (x+int(math.sqrt(x))+1)%n
def f7(x,n): return (x*x +3)%n

def rho(n, f=f1):
  x = 2
  y = 2
  d = 1
  while d==1:
    x = f(x,n)
    y = f(f(y,n),n) 
    d = gcd(abs(x-y),n)
  if d==n:
    return False
  return d

def prime_factors(n):
  factors = set()
  i = 2
  while i*i <= n:
    while (n % i) == 0:
      factors.add(i)
      n = n / i
    i += 1
  if n > 1:
    factors.add(n)
  return factors

# returns how many times (in percentual), a function f fails when used by
# pollars rho method for numbers up to n
def test_correct(f,n=100):
  fails = 0
  for i in xrange(2,n):
    rho_i = rho(i,f)
    if(rho_i==False):
      factors = prime_factors(i)
      if (len(factors)!=1):
        fails += 1
    else:
      if (i % rho_i != 0):
        fails += 1
  return 100*fails/float(n)

# function to be used by benchmark. runs rho using f from 2 to n.
def benchmark(f,n):
  for i in xrange(2,n):
    rho_i = rho(i,f)

if __name__ == '__main__':
  n = 10
  for f in f1, f2, f3, f4, f5, f6, f7:
    fname = f.func_name
    fails = str(test_correct(f,n))+"%"
    performance = timeit.timeit("benchmark({}, {})".format(fname, n), setup="from __main__ import rho, {}, benchmark".format(fname))
    print "Function: {}, Fails: {}, Performance: {}, n={}".format(fname, fails, performance, n)
 
