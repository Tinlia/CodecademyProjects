# Evan "Tinlia" Kimpton
# Given an array of numbers, return the xth number in order
def getX(x, nums):
    # Parameter checks
    if x > len(nums): return 0
    if not nums: return 0
    # Sort the array
    nums.sort()
    # Find the xth number
    for i in range (len(nums)+1):
        if i == x-1: return nums[i]

print(getX(2, [6, 3, -1, 5]))
