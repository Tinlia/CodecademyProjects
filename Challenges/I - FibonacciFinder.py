# Evan "Tinlia" Kimpton
# Create a program that takes a number and prints the corresponding Fibonacci number.
# Assume n=1 returns 0 and n=2 returns 1
def fib_finder(n):
  a, b, total = 0, 1, 0   # The first two numbers of the Fibonacci order are 0,1
  if n == 2: return 1     # Base Case
  for i in range(1,n-1):  
    total = a + b         # Acts as both a hold value and the total
    a, b = b, total       # Shift values left i.e., 0+1=1 -> 1+1=2 -> 1+2=3
  return total

print(fib_finder(10))
