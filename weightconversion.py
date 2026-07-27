import math
print("This is a weight conversion program from Kilograms to Pounds\n By:Yosef Shamoug")

useround = math.ceil(float(input("To how many digits do you want to round\n (Up to 10 digits)")))
while useround > 10:
  print("That is not a valid value")
  useround = math.ceil(float(input("To how many digits do you want to round\n (Up to 10 digits)")))

conversion = input("What are you converting from(kg or lbs)")
weight = input(f"what is the weight in {conversion}")
if conversion == 'kg':
  print(f"{weight} kilograms is equivalent to {round(float(weight)*2.205,useround)} pounds")
else:
  print(f"{weight} pounds is equivalent to {round(float(weight)/2.205,useround)} kilograms")