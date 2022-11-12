# A simple program to practice creating and manipulating 2D arrays 
first_names = ['Ainsley', "Ben", "Chani", "Depak"]
preferred_size = ["Small", "Large", "Medium"]
preferred_size.append("Medium")
print(preferred_size)
customer_data = [
  ["Ainsley", "Small", True],
  ["Ben", "Large", False],
  ["Chani", "Medium", True],
  ["Depak", "Medium", False]
]
print(customer_data)

# Chani no longer wants expedited shipping, update the list to reflect this
customer_data[2][2] = False

# Ben no longer wants a shipping option, update the list to reflect this
customer_data[1].remove(False)

# Add two new customers to the list of customer data
customer_data_final = customer_data + [
  ["Amit", "Large", True],
  ["Karim", "X-Large", False]
]
print(customer_data_final)
