current_budget = 3500.75

def print_remaining_budget(budget):
  print("Your remaining budget is: $" + str(budget))

print_remaining_budget(current_budget)


def deduct_expense(budget, expense):
  return budget-expense

shirt_expense = 9
new_budget_after_shirt = deduct_expense(current_budget,shirt_expense)

print(new_budget_after_shirt)
print_remaining_budget(new_budget_after_shirt)
