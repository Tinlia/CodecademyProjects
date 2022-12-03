# Evan "Tinlia" Kimpton
# Create a program that sorts scores from greatest to lowest
# Note: This project must be done without the sort() method
def score_sorter(a):
    while True:
        check = True
        for i in range(0, len(a) - 1):
            if a[i] < a[i + 1]:
                hold = a[i]
                a[i] = a[i + 1]
                a[i + 1] = hold
                check = False
        if check: return a

score_list = [1, 2, 3, 9999, 13]
print(score_sorter(score_list))
