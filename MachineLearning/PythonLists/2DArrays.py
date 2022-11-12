# A short program to practice 2D Arrays

#Students, Heights, and Ages
heights = [["Jenny", 61], ["Alexus", 70], ["Sam", 67], ["Grace", 64], ["Vik", 68]]

ages = [["Aaron", 15], ["Dhruti",16]]

tictactoe = [
  ["X","O","X"],
  ["O","X","O"],
  ["o","O","X"]
]

#Students and Scores
class_name_test = [
  ["Jenny", 90],
  ["Alexus", 85.5],
  ["Sam", 83],
  ["Ellie", 101.5]
]
print(class_name_test)

sams_score = class_name_test[2][1]
print(sams_score)

ellies_score = class_name_test[-1][-1]
print(ellies_score)

#Incoming students, their nationalities, and their grade
incoming_class = [
  ["Kenny", "American", 9],
  ['Tanya', "Russian", 9],
  ["Madison", "Indian", 7]
]
print(incoming_class)

  #Move Madison from grade 7 to grade 8
incoming_class[2][2] = 8
print(incoming_class)

  #Change Kenny to Ken using only negative indices
incoming_class[-3][-3] = "Ken"
print(incoming_class)
