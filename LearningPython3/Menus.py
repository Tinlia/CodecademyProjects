# The purpose of this document is to practice Classes, constructors, and methods by creating imaginary restaurant chains with their individual menus

# Menu Class
class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time
  
  def __repr__(self):
    return "{name} menu available from {start} to {end}".format(name=self.name, start=self.start_time, end=self.end_time)

  # Calculates the cost of items entered
  def calculate_bill(self, purchased_items):
    total = 0
    for item in purchased_items:
      total += self.items[item]
    return total

class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus
  
  def __repr__(self):
    return "A new franchise has been made, located at {address}".format(address=self.address)

  def available_menus(self, time):
    available = []
    if 11 <= time <= 15: available.append('Brunch')
    if 15 <= time <= 18: available.append('Early Bird')
    if 17 <= time <= 23: available.append('Dinner')
    if 11 <= time <= 21: available.append('Kids')
    return "The following menus are available at {time}:00 -- {available}".format(time=time, available=available)

class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises

#-# Menus #-#
# Brunch Menu
brunch = Menu("Brunch", {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}, "11am", "4pm")

# Early Bird Menu
early_bird = Menu("Early Bird", {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}, "3pm", "6pm")

# Dinner Menu
dinner = Menu("Dinner", {
  'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}, "5pm", "11pm")

# Kids Menu
kids = Menu("Kids", {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}, "11am", "9pm")

# Arepas Menu
arepas_menu = Menu("Arepas Menu", {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}, "10am", "8pm")

#-# Franchises #-#
# Main Store
flagship_store = Franchise("1232 West End Road", [brunch, early_bird, dinner, kids])

# New Store
new_installment = Franchise("12 East Mulberry Street", [brunch, early_bird, dinner, kids])

# Take a' Arepa
arepas_place = Franchise("189 Fitzgerald Avenue", arepas_menu)

#-# Businesses #-#
# Basta Fazoolin' with my Heart init
basta = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])

arepa = Business("Take a' Arepa", [arepas_place])

# Test Cases
print(brunch)
print(flagship_store)
print(flagship_store.available_menus(17))
print("Total cost: $" + str(brunch.calculate_bill(['pancakes', 'home fries', 'coffee'])))
print("Total cost: $" + str(early_bird.calculate_bill(['mushroom ravioli (vegan)', 'salumeria plate'])))
