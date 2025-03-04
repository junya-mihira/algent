def sieve_prime(n: int) -> list[int]:
    primes = [True]*(n+1)
    primes[0] = False
    primes[1] = False
    for i in range(2, int(n**0.5)+1):
        if primes[i]:
            for j in range(i*2, n+1, i):
                primes[j] = False
    return [i for i in range(n+1) if primes[i]]


if __name__ == '__main__':
    ans = sieve_prime(30)
    print(ans)
