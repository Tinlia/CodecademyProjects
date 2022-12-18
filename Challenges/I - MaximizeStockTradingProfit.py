# Evan "Tinlia" Kimpton
# Goal: given an array of stock prices in a week, return the best buy and sell date to generate the most profit
# i.e., Input: [17, 11, 60, 25, 150, 75, 31, 120] Output: (1,4)
def max_profit_days(stock_prices):
  hold = [0,0,0] 
  for x in range(0, len(stock_prices)):     # Nested loop, first loop checks each date
    for y in range(x, len(stock_prices)):   # Nested loop, second loop finds the greatest diff between x and all other days
      if stock_prices[y] - stock_prices[x] > hold[2]:                     # If the difference is the largest, 
        hold[0], hold[1], hold[2] = x, y, stock_prices[y]-stock_prices[x] # record the buy/sell date and the diff
  if hold[0] == hold[1]: hold[1] += 1       # Prevents the buy/sell dates from being the same
  return hold[0], hold[1]                   # return buy date, sell date

print(max_profit_days([150, 150, 1]))
