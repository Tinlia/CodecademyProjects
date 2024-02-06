# Evan "Tinlia" Kimpton
# Create a program that takes an integer n and return the sum of its prime factors

def sum_of_prime_factors(n):
    primes = 0
    for i in range(2,n+1):
        for j in range(2,i):
            if i % j == 0 : break
        else : primes += i
    return primes

print(sum_of_prime_factors(11)) # 28