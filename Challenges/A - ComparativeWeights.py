# Evan "Tinlia" Kimpton
# Goal: You are given "n" balls, one of which weighs differently than the others. 
# You also have a scale that can fit an infinite number of balls on either side.
# Return the least amount of tests you need to perform to find the odd ball out
def scale_of_truth_n(n):
    count, exponent = 2, 1
    while True:
        if n < count: return exponent - 1  # It's fairly difficult to explain this without showing it, but this performs
        count += 2 * (3 ** (exponent - 1)) # a custom algorithm I made to determine the minimum number of scale tests needed (see line 14+)
        exponent += 1

print(scale_of_truth_n(4))

# Balls / Tests
# 1  0            1 - 2   2 - 6   3 - 18   4 - 54 
# 2  1            Notice for each amount of tests required, the number of occurrences multiplies by 3: 2*3 = 6, 6*3 = 18, 18*3 = 54
# 3  1            To determine the ranges for at which point the number of test req. increases, I used lines 7-10
# 4  2            i.e., if n is between 24-27, return the exponent of 3 subtracted by one, which would return 3
# 5  2
# 6  2            I have trouble explaining it, but on paper it might be easier.
# 7  2
# 8  2
# 9  2
# 10 3
# 11 3
# 12 3
# 13 3
# 14 3
# 15 3
# 16 3
# 17 3
# 18 3
# 19 3
# 20 3
# 21 3
# 22 3
# 23 3
# 24 3
# 25 3
# 26 3
# 27 3
# 28 4
# ...
# 81 4
# 82 5
