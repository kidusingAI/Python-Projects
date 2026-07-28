food = []
price = []
total = 0
item = 0
while item != '':
  item = input("What food do you want to buy(press enter to quit)")
  if item == '':
    break
  else:
    food.append(item)
    cost = float(input("enter a price for the food"))
    price.append(str(cost)) 
    total = total+cost
print("----- YOUR CART -----")
x = 0
for foods in food:
  print(f"{food[x]:<30} $             {float(price[x]):>.2f}")
  x = x+1
print(f"Your total is \n${total:04.2f}")
