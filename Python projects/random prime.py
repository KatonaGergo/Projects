'''
def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

primes = []

for i in range(2, 250001):
    if is_prime(i):
        primes.append(i)


print(len(primes))
'''

import math


def is_prime(n):
    
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

primes = []


for i in range(2, 10):
    if is_prime(i):
        primes.append(i)

print(len(primes))