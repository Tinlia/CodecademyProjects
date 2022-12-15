# Evan "Tinlia" Kimpton
# Given an input phrase, reverse the word order but not the letter order
# Input: "My Name Is Evan" Output: "Evan Is Name My"
def word_reverser(phrase):
    word, reverse, hold = "", "", []
    for x in phrase:
        if x != ' ': word += x
        else:
            hold.append(word)
            hold.append(" ")
            word = ""
    hold.append(word)
    hold.reverse()
    for x in hold: reverse += x
    return reverse


print(word_reverser('Hello Worlds'))
