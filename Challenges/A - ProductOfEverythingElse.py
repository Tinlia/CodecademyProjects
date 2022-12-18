# Evan "Tinlia" Kimpton
# Given an array of integers, return an array containing the product of all other integers in the array
# Example - Input: [1,2,3] Output: [6,3,2]
def product_of_the_others(array):
    return_array = []                # Array init
    for x in range(len(array)):      # Nested for loop, first iterates through every number
        product = 1                  # Because if it was 0, product would never change
        for y in range(len(array)):  # Nested for loop, second iterates through every other number
            if x != y:               # If not the same element in the list, multiply by the other elements
                product *= array[y]  
        return_array.append(product) # When done iterating, add to updated array
    return return_array


print(product_of_the_others([1, 2, 3]))
