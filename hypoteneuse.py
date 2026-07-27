import math
useround = math.ceil(float(input("To how many digits do you want to round\n (Up to 10 digits)")))
while useround > 10:
  print("That is not a valid value")
  useround = math.ceil(float(input("To how many digits do you want to round\n (Up to 10 digits)")))

a = input("what is the length of the first side")
b = input("what is the length of the second side")
c = math.sqrt(float(a)**2+float(b)**2)
if int(c) == c: #coincidence of the smiley face but nice
  print(f"the length of the hypoteneuse is {int(c)}")
else:
  print(f"the approximate length of the hypoteneuse is {round(c,useround)}")