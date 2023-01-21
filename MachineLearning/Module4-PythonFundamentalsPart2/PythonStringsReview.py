# Create a function that takes a first and last name and produces a username. 3 letters from first name, 4 letters from last name
def username_generator(first_name, last_name):
  firstMax, lastMax = 3, 4
  if len(first_name) <= 3: firstMax = len(first_name) 
  if len(last_name) <= 4: lastMax = len(last_name) 
  return first_name[:firstMax] + last_name[:lastMax]

# using the generated username, create a password by shifting the letters in the username one to the right
def password_generator(user_name):
  password = ""
  for i in range(0, len(user_name)):
    password += user_name[i-1]
  return password
