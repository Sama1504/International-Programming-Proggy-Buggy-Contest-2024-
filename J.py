N = int(input())

if not (0 <= N <= 10**7):
    print("Invalid input")
else:
    prime_count = {}
    
    for n in range(N + 1):
        f_n = n**2 - 79*n + 1601
        if sympy.isprime(f_n):
            if f_n in prime_count:
                prime_count[f_n] += 1
            else:
                prime_count[f_n] = 1
    
    repeating_primes = sum(1 for count in prime_count.values() if count > 1)
    print(repeating_primes)