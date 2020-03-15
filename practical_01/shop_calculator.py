# number of items
# price of items
# 10% discount if price is over $100

i = 0
total_price = 0
number_of_items = int(input("Enter Number Of Items Please: "))
while i < number_of_items:
    price_of_item = float(input("PLease Enter Cost of Item: $"))
    total_price = total_price + price_of_item
    i = i + 1
if total_price < 100:
    print("Your Total Is $", total_price)
else:
    discount_price = total_price * 0.9
    print("Your Total Is $", discount_price)
