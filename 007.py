def isPrime(n):
    if n <= 1:
        return False

    # Check divisibility from 2 to n-1
    for i in range(2, n):
        if n % i == 0:
            return False

    return True

primes = []
i = 0
while (len(primes) < 10002):

    if (isPrime(i)):

        primes.append(i)
    
    i += 1

print(primes[10000])