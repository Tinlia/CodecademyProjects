# Evan "Tinlia" Kimpton
# Goal: You are given "n" balls, one of which weighs differently than the others. 
# You also have a scale that can fit an infinite number of balls on either side.
# Return the least amount of tests you need to perform to find the odd ball out
def scale_of_truth_n(n):
    count, exponent = 2, 1
    while True:
        if n < count: return exponent - 1  
        count += 2 * (3 ** (exponent - 1)) 
        exponent += 1

print(scale_of_truth_n(4))