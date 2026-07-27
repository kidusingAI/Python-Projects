import math
useround = math.ceil(float(input("To how many digits do you want to round\n (Up to 10 digits)")))
while useround > 10:
  print("That is not a valid value")
  useround = math.ceil(float(input("To how many digits do you want to round\n (Up to 10 digits)")))
  
diameter = (input("Input the diameter here if you need radius just press enter"))
if bool(diameter) == False:
  radius = input("Input the radius")
  circumference = math.pi*2*float(radius)
  print(f"The circumference is approximately {round(circumference,useround)}")
else:
  circumference = math.pi*float(diameter)
  print(f"The circumference is approximately {round(circumference,useround)}")