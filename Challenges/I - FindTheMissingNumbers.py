# Evan "Tinlia" Kimpton
# Create a program that takes a list of numbers and returns the missing numbers in a list
def missing_nos(arr, k):
  missing = []
  for i in range(0, len(arr) - 1):
    if arr[i] + 1 != arr[i+1]:
      missing.append(arr[i] + 1)    
  return missing

print(missing_nos([1, 2, 4, 5, 6, 7, 8, 10], 2)) # [3, 9]
