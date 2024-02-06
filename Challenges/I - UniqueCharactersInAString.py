# Evan "Tinlia" Kimpton
# Create a program that takes in a String and returns if all the characters are unique or not

def unique_characters(s):
    return len(s.lower()) == len(set(s.lower()))

print(unique_characters("Apple")) # False