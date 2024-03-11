# Create menu
menu = ["Coffee" , "Tea", "Cake" , "Sandwich"]
# Create stock list
stock = {
    "Coffee": 100,
    "Tea": 50,
    "Cake": 30,
    "Sandwich": 20
}
# Create price list
price = {
    "Coffee": 2.0,
    "Tea": 1.5,
    "Sandwich": 3.0,
    "Cake": 4.5
}
# Calculate total stock worth
total_stock_worth = 0.0
for item in menu :
    item_value = stock[item] * price[item]
    total_stock_worth += item_value
# Print out result
print(f"The total stock in cafe is worth for $ {total_stock_worth}. ")

