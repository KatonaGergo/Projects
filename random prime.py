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