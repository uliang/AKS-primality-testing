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

import math
import decimal
from decimal import Decimal
import sys

if sys.version_info < (3,):
    input = raw_input


def check_poly_congruence(r, n):
    pass


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
    ctx.prec = 102
    tol = Decimal('1E-99')

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
        #print("{} {}".format(p, n%p))
        if n % p == 0:
            while n % p == 0:
                n = n//p

            result -= result//p
        #print(result)
        p += 1
        #print("{} {} n={}".format(p, result,n ))

    if n > 1:
        result -= result//n

    return result


def main():

    n = input("Enter prime\n>>")
    n = int(n)

    if perfect_power(n):
        return "Composite"

    r = get_r(n)

    for a in range(2, min(r, n-1)+1):
        if n % a == 0:
            return "Composite"

    if n <= r:
        return "Prime"


if __name__ == "__main__":
    print(sys.version_info)
    main()
