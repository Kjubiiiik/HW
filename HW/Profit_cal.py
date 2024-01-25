#You work for a manufacturer, and have been asked to calculate the total profit made on the sales of a product. 
#You are given a dictionary containing the cost price per unit (in dollars), sell price per unit (in dollars), and the starting inventory. 
#Return the total profit made, rounded to the nearest dollar.

cost_price = float(input("Zadejte výrobní cenu produktu: "))
sell_price = float(input("Zadejte cenu produktu: "))
inventory = int(input("Zadejte kolik bylo vyrobeno produktů: "))

def Profit_cal(cost_price, sell_price, inventory):
    profit = (sell_price * inventory) - (cost_price * inventory)
    return round(profit)
print(Profit_cal(cost_price, sell_price, inventory))