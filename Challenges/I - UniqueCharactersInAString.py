# Evan "Tinlia" Kimpton
# Create a program that takes in a String and returns if all the characters are unique or not
def unique_characters(string_in):
    if string_in == "":
        return "Error, invalid input"
    a = []
    lettList = list(string_in.lower())
    for i in lettList:
        check = True
        for j in a:
            if i == j: check = False
        if check: a.append(i)
        else: return False
    return True

print(unique_characters("Apple"))


# Below is a more compact version, but takes longer to perform

# def unique_characters(s):
#     c = 1
#     word = s.lower()
#     if s == "": return "Invalid input"
#     for x in word:
#         if x in word[c:]: return False
#         c += 1
#     return True
