# Evan "Tinlia" Kimpton
# Create a program that takes a list of numbers and returns the missing numbers in a list
def missing_nos(arr, k):
  a=[]
  i, j = 0, 0
  while i < len(arr):
    if j != arr[i]:
      a.append(arr[i]-1)
      j = j+2
    else : j= j + 1
    i= i+1
  a.remove(0)
  return a

print(missing_nos([1, 2, 4, 5, 6, 7, 8, 10], 2))
