# Evan "Tinlia" Kimpton
# Create a program that takes a number and prints the corresponding Fibonacci number.
# Assume n=1 returns 0 and n=2 returns 1
def fib_finder(n):
  a, b, total = 0, 1, 0
  if n == 2: return 1
  for i in range(1,n-1):
    total = a + b
    a, b = b, total
  return total

print(fib_finder(10))
