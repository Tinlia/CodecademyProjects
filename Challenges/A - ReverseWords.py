# Evan "Tinlia" Kimpton
# Given an input phrase, reverse the word order but not the letter order
# Input: "My Name Is Evan" Output: "Evan Is Name My"

def word_reverser(phrase):
    return ' '.join(phrase.split()[::-1])

print(word_reverser('Hello Worlds')) # Worlds Hello
