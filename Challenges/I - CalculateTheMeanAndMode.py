# Evan "Tinlia" Kimpton
# Goal: create a function that takes an array of integers and returns the mean and the lowest mode
import statistics as s

def stats_finder(a):
  a.sort()
  return [ (sum(a) / len(a)) , s.mode(a) ]

print(stats_finder([500, 400, 400, 375, 300, 350, 325, 300])) # [368.75, 300]
