# Evan "Tinlia" Kimpton
# Given an input phrase, reverse the word order but not the letter order
# Input: "My Name Is Evan" Output: "Evan Is Name My"
def word_reverser(phrase):
    word, reverse, hold = "", "", []
    for x in phrase:                  # Turns the string into a char array without reinitializing
        if x != ' ': word += x        
        else:                         # When the end of a word is found, save the word to an array of words
            hold.append(word)
            hold.append(" ")          # Add a space
            word = ""
    hold.append(word)                 # Add the last word, no space
    hold.reverse()                    # Reverse the word order
    for x in hold: reverse += x       # Convert array to string
    return reverse


print(word_reverser('Hello Worlds'))
