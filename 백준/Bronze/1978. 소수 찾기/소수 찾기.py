import sys

n = int(sys.stdin.readline())
primes = list(map(int, sys.stdin.readline().split()))
prime_cnt = 0

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

for prime in primes:
    if prime == 1:
        continue
    if is_prime(prime):
        prime_cnt += 1

print(prime_cnt)