# Goal: create a small program to generate a password from the last three letters of an employee's first and last name

first_name = "Evan"
last_name = "Kimpton"

def password_generator(first_name, last_name):
  return first_name[len(first_name)-3:] + last_name[len(last_name)-3:]

temp_password = password_generator(first_name, last_name)
