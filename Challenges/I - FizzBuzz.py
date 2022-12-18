# Evan "Tinlia" Kimpton
# Replace every multiple of 3 with Fizz, 5 with Buzz, and multiples of 3 and 5 with FizzBuzz
# Return as an array
def fizzbuzz(limit):
  a = []
  for i in range(1,limit+1):
    if i%3 == 0 and i%5 == 0: a.append("FizzBuzz") # If 3 and 5, FizzBuzz
    elif i%3 == 0: a.append("Fizz")                # If 3, Fizz
    elif i%5 == 0: a.append("Buzz")                # If 5, Buzz
    else: a.append(i)                              # If neither, keep the number
  return a

print(fizzbuzz(16))
