# Evan "Tinlia" Kimpton
# Create a program that sorts scores from greatest to lowest
# Note: This project must be done without the sort() method
def score_sorter(a):
    return [a.pop(a.index(max(a))) for _ in range(len(a))]

score_list = [1, 2, 3, 9999, 13]
print(score_sorter(score_list))
