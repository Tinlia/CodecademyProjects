# Evan "Tinlia" Kimpton
# Create a program that takes in a String and returns if all the characters are unique or not
def unique_characters(string_in):
    if string_in == "":
      return "Error, invalid input"
    a = []
    if not string_in: return True
    letList = list(string_in.lower())
    for i in letList:
        check = True
        for j in a:
            if i == j:
                check = False
        if check:
            a.append(i)
        else:
            return False
    return True

print(unique_characters("Apple"))
