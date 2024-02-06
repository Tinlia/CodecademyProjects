# Evan "Tinlia" Kimpton
# Create a program that returns an array of prime numbers from 2 to n
def prime_finder(x):
    primes = []
    for i in range(2,x):
        for j in range(2,i):
            if i % j == 0 : break
        else : primes.append(i)
    return primes

print(prime_finder(11)) # [2, 3, 5, 7, 11]
