# Evan "Tinlia" Kimpton
# Create a program that returns an array of prime numbers from 2 to n
def prime_finder(n):
    a = []
    for i in range(2, n + 1):
        prime = True
        for j in range(2, i):
            if i % j == 0:
                prime = False
                break
        if prime: a.append(i)
    return a

print(prime_finder(11))
