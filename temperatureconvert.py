import math
print("This is a temperature conversion program from Celsius to Farenheit\n By:Yosef Shamoug")

useround = math.ceil(float(input("To how many digits do you want to round\n (Up to 10 digits)")))
while useround > 10:
  print("That is not a valid value")
  useround = math.ceil(float(input("To how many digits do you want to round\n (Up to 10 digits)")))

conversion = input("What are you converting from(Celsius or Farenheit capital letters are important)")
temperature = input(f"what is the temperature in {conversion}")
if conversion == 'Celsius':
  print(f"{temperature} Celsius is equivalent to {round((float(temperature)*9/5)+32,useround)} Degrees Farenheit")
else:
  print(f"{temperature} Farenheit is equivalent to {round((float(temperature)-32)*5/9,useround)} Degrees Celsius")