# Evan "Tinlia" Kimpton
# Goal: create a function that takes an array of integers and returns the mean and the lowest mode

def stats_finder(a):
  a.sort(reverse=True) # If the lowest mode is wanted, there's no need to compare which mode is 
                       # smaller later on. If the same number of occurrences happen it will always be the new mode
  c=1                  # of times a number occurs, starting at 1
  mm = []              # Mean / Mode
  mode = [a[0],1] 
  mm.append( sum(a) / len(a) ) # Adds the mean
  for x in range(1,len(a)):
    if a[x-1] == a[x]: c+=1       # If the previous number is equal to the current one, increase occurrences by 1
    else: c=1                     # Else, it's the last occurrence 
    if c >= mode[1]:              # If most, or equal occurrences of a number, becomes the new mode
      mode[0], mode[1] = a[x], c  # Mode, number of times in array
  mm.append(mode[0])              # Add the mode
  return mm

print(stats_finder([500, 400, 400, 375, 300, 350, 325, 300]))
