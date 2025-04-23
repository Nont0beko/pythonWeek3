def calculate_discount(price,discount_percent):
  discounted = price * (discount_percent / 100)
  original_price = price - discounted
  return original_price 
prompt1 = float(input("Enter the original price of the item"))
prompt2 = float(input("Enter the discount percentage of the item"))

final_price = calculate_discount(prompt1, prompt2)

print("Final price:"+ str(final_price))