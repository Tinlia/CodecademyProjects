# Create a function that takes in two strings and returns the unique letters they share
def common_letters(string_one, string_two):
  a, c = [], 0
  for x in string_one:
    if( x in string_two) and not (x in string_two[:c]): a.append(x)
    c+=1
  return a
