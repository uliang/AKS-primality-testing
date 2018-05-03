"""
This is an implementation of the AKS primality test by Agrawal, Kayal and
Saxena (2004) in Python.

The algorithm outline:

Input n > 1

1. Check that n is not a perfect power a^b for some a>1 and b>1.
   If it is output composite

2. Find smallest r such that ord_r(n) > (log_2 n)^2. Skip this r if
   gcd(r,n) != 1

3. For all 2 <= a <= min(r, n-1), check a does not divide n. Otherwise output
   composite.

4. If n <= r output prime.

5. For a = 1 to floor( sqrt(totient(r)) log2(n)) do
        if (X + a)^n != X^n +a mod (X^r -1, n) output composite

6. Output prime.


References:
    PRIMES is in P, Annals of Mathematics. 160 (2): 781-793
_________________________________________________________________________

Author: Tang U-Liang
Email: tang_u_liang@sp.edu.sg
_________________________________________________________________________
"""

from sympy import div, Symbol, Poly, expand
from sympy.abc import x
import math
import decimal
from decimal import Decimal
import sys

if sys.version_info < (3,):
    input = raw_input


def check_poly_ncongruence(r, n):
    L = math.floor(math.sqrt(totient(r))*math.log(n, 2))
    a = Symbol('a')
    _, rem = div((x+a)**n - (x**n+a), x**r-1, domain="ZZ")
    #Possible Alternate calculation for rem
    #rem = poly_power_mod(x+a, n, x**r-1)
    #_, rem2 = div(x**n-a, x**r-1, domain="ZZ")
    #rem -= rem2
    rem.map_coeffs(lambda c: c%n)
    aa = 1
    while aa <= L:
        remAA = rem
        remAA.subs({a:aa})
        remAA.map_coeffs(lambda c: c%n)
        if remAA != 0:
            return False
        aa += 1
    return True


def poly_power_mod(base, exponent, quotient):
   """
   Needs vetted for matematical accuracy
   usese same theory as power_mod over the integers
   except applied to polys using remainders
   (i just kinda assumed it was isomorphic)
   """
   ret = 1
   _, base = div(base, quotient, domain="ZZ")
   while exponent > 0:
      if exponent%2 == 1:
         _, ret = div(ret*base, quotient, domain="ZZ")
         
      exponent=exponent//2
      _, base = div(base*base, quotient, domain="ZZ")
      
   return ret


def gcd(m, n):
    while m % n != 0:
        m, n = n, m % n

    return n


def order(r, n):
    """
    Calculates the multiplicative order of n modulo r.

    e.g.
    order(8,3) = 2
    order(15,2) = 4
    order(8, 65) = 1
    order(3, 5) = 2
    order(6, 4) = False as 4 is not coprime to 6.

    Returns
       *int*,
       k such that r^k is congruent to 1 mod n
       bool, False if n and r are not coprime.
    """
    if gcd(r, n) != 1:
        return False

    i = 1
    while pow(n, i, r) != 1:
        i += 1
    return i


def get_r(n):
    """
    Performs the search for r in the second step of AKS algorithm.

    e.g.
    get_r(31) = 29

    Returns
        *int*,
        smallest r such that r and n are coprime such that
        order_r(n) > (log_2(n))^2.
    """
    r = 2
    L = (math.log(n, 2))**2

    while True:
        if gcd(r, n) == 1:
            if order(r, n) > L:
                return r
        r += 1


def perfect_power(n):
    """
    Checks that n is a perfect power i.e. n=a^b for a>1 and b>1

    Returns
        *bool*,
        True indicates that it is a perfect power. Therefore,
        False indicates that the algorithm continues.
    """
    ctx = decimal.getcontext()
    ctx.prec = 12
    tol = Decimal('1E-9')

    # print(ctx)
    M = math.ceil(math.log(n, 2))
    for b in range(2, M):

        a = ctx.power(n, ctx.power(b, -1))
        # print(a)

        if abs(ctx.to_integral_exact(a)-a) <= tol:
            return True

    return False


def totient(n):
    """
    Returns
        *int*,
        the number of integers k such that gcd(k,n) = 1.
    """
    result = n
    N = n
    p = 2
    while p*p < N:
        if n % p == 0:
            while n % p == 0:
                n = n//p

            result -= result//p
        p += 1

    if n > 1:
        result -= result//n

    return result


def main(n):

    if perfect_power(n):
        return "Composite"
    print("Checked perfect power")

    r = get_r(n)
    for a in range(2, min(r, n-1)+1):
        if n % a == 0:
            return "Composite"
    print("Checked {} has no small number divisors".format(n))

    if n <= r:
        return "Prime"

    print("Begin polynomial congruence test")
    if check_poly_ncongruence(r, n):
        return "Prime"


if __name__ == "__main__":
    print(sys.version_info)
    n = input("Enter prime\n>>")
    n = int(n)
    isPrime = main(n)
    print(isPrime)
