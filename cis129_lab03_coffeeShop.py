print("My Coffee and Muffin Shop Receipt")

def calculate_total_cost(coffee_amount, muffin_amount, boba_amount, tea_amount):
    #Prices
    coffee_price = 5
    muffin_price = 4
    boba_price = 4
    tea_price = 3
    tax_rate = .06
    
    #Subtotal
    subtotal = (coffee_amount * coffee_price) + (muffin_amount * muffin_price) + (boba_amount * boba_price) + (tea_amount * tea_price)
    
    #Taxes
    tax_amount = subtotal * tax_rate
    
    #Total Cost
    total_cost = subtotal + tax_amount
    
    return total_cost
    
#Customer's order
coffee_amount = int(input("Amount of Coffees: "))
muffin_amount = int(input("Amount of Muffins: "))
boba_amount = int(input("Amount of Boba: "))
tea_amount = int(input("Amount of Tea: "))

#Calculate total cost 
total_cost = calculate_total_cost(coffee_amount, muffin_amount, boba_amount, tea_amount)

#Final Result
print("\nTotal Cost: $", total_cost, "\n\nThank you for your purchase!")
