# Create a function named calculate_discount(price, discount_percent) that calculates the final price after applying a discount. The function should take the original price (price) and the discount percentage (discount_percent) as parameters. If the discount is 20% or higher, apply the discount; otherwise, return the original price.
# Using the calculate_discount function, prompt the user to enter the original price of an item and the discount percentage. Print the final price after applying the discount, or if no discount was applied, print the original price.
import time

def calculate_discount(price, discount_percent):
  if discount_percent >= 20:
    return price * (1- discount_percent / 100)
  return price
print("🎉 Welcome to the cashier calculator 🎉\n")

time.sleep(1)
total_amount = 0
try:
  while True:
    price = float(input("\nEnter the original price of the item: "))

    time.sleep(2)

    discount_percent = float(input("\nEnter the discount percentage: "))

    time.sleep(2)

    if price <= 0 or discount_percent < 0:
      print("❌ Error! Invalid input! Please number more than zero😁")
    else: 
      total_price = calculate_discount(price,discount_percent)
      total_amount += total_price
      print(f"\n🤑 The amount is ksh.{total_price:.2f}\n") 
      next_transaction = input("Is there another transaction? (y/n): ")
      if next_transaction == "y":
        continue
      elif next_transaction == "n":
           
        print(f"\n🤑 The total amount is ksh.{total_amount:.2f}\n")
        time.sleep(1)
        print("Thank you! for using cashier calculator😊") 
        break
       

except ValueError:
  print("❌ Error! Please input a valid number😊")

