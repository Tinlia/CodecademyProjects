# Evan "Tinlia" Kimpton
# Create a program that takes an integer n and return the sum of its prime factors

def prime_finder(x,y):
    for i in range (2,x):
        if x % i == 0 : return 0
    if y % x == 0 : return x
    else : return 0

def sum_of_prime_factors(n):
    total = 0
    for i in range(2,n+1):
        total = total + prime_finder(i,n)
    return total

print(sum_of_prime_factors(91))
