# Evan "Tinlia" Kimpton
# Given an array of numbers, return the xth number in order
def getX(x, nums):
    nums.sort()
    return 0 if (x > len(nums) or x<1) else nums[x-1]

print(getX(2, [6, 3, -1, 5])) # 3