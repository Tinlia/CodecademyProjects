# Evan "Tinlia" Kimpton
# Given an array of integers, return an array containing the product of all other integers in the array
# Example - Input: [1,2,3] Output: [6,3,2]
def product_of_the_others(array):
    return_array = []
    for x in range(len(array)):
        product = 1
        for y in range(len(array)):
            if x != y:
                product *= array[y]
        return_array.append(product)
    return return_array


print(product_of_the_others([1, 2, 3]))
