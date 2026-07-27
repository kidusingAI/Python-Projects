import math
useround = math.ceil(float(input("To how many digits do you want to round\n (Up to 10 digits)")))
while useround > 10:
  print("That is not a valid value")
  useround = math.ceil(float(input("To how many digits do you want to round\n (Up to 10 digits)")))

radius = input("Input the radius here if you need diameter just press enter")
if bool(radius) == False:
  diameter = float(input("Input the diameter"))
  area = math.pi*(diameter/2)**2
  print(f"The area is approximately {round(area,useround)}")
else:
  area = math.pi*int(radius)**2
  print(f"The area is approximately {round(area,useround)}")