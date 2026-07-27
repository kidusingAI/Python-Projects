item = input("What item are you buying")
print("I dont care anyways it doesnt matter to this program only the quantity and price do")
quantity = int(input("How many items are you buying"))
price = float(input("what does one unit of this item cost"))
total = quantity*price
if total == int(total):
  print(f"your total is {int(total)}")
else:
  print(f"your total is {total}")