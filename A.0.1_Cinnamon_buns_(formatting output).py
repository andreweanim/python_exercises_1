# Defining the prices
regular_price = 35.00

discount_rate = 60/100

# user input
num_old_kanelbulle = int(input("How many day-old Kanelbulle do you want to buy? "))

# costs
total_regular_price = num_old_kanelbulle * regular_price
discount_amount = total_regular_price * discount_rate
total_price = total_regular_price - discount_amount

# results
print(f"Regular price: {total_regular_price:.2f} SEK")
print(f"Discount: {discount_amount:.2f} SEK")
print(f"Total price: {total_price:.2f} SEK")