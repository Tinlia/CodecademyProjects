# Evan "Tinlia" Kimpton
# Replace every multiple of 3 with Fizz, 5 with Buzz, and multiples of 3 and 5 with FizzBuzz
def fizzbuzz(limit):
  types = {
    3: "Fizz",
    5: "Buzz"
  }
  a = []
  for i in range(1,limit+1):
    s = ""
    for type in types:
      if i % type == 0:
        s += types[type]
    a.append(i if s=="" else s)
  return a

print(fizzbuzz(16)) # [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz', 16]
