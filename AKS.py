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


def gcd(m,n):
    while m%n != 0:
        m, n = n, m%n

    return n

def not_perfect_power(n):
    """
    Checks that n is not a perfect power i.e. n=a^b for a>1 and b>1
    
    Returns
        bool, True indicates that it is not a perfect power. Therefore,
              False indicates that n is composite
    """
    M = math.floor(math.log(n, 2))+1
    
    for b in range(2, M):
        a = pow(n, 1/b)
        
        if math.floor(a)-a == 0:
            return False
    return True

