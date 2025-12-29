def sieve_of_eratosthenes(limit):
    sieve = [True] * (limit + 1)
    sieve[0:2] = [False, False]  # 0 and 1 are not primes
    
    for i in range(2, int(limit ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, limit + 1, i):
                sieve[j] = False
    return [i for i, prime in enumerate(sieve) if prime]

# Example
start, end = 10, 50
all_primes = sieve_of_eratosthenes(end)
primes_in_range_list = [p for p in all_primes if p >= start]
print(f"Primes between {start} and {end}:", primes_in_range_list)
