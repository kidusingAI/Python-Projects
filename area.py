length = float(input("What is the length of the rectangle in centimeters"))
width = float(input("What is the width of the rectangle in centimeters"))
area = length * width
if area == int(area):
  print(f"your area is {int(area)} centimeters squared!")
else:
  print(f"your area is {area} centimeters squared!")