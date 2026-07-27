userinput = int(input("How many characters in the password"))
randomletters = list()
def passwordgenerator():
  global userinput
  global x
  global y
  global password
  import random
  import string
  numbers = string.digits
  letters = string.ascii_letters
  symbols = string.punctuation
  fullist = numbers + letters + symbols
  for x in range(userinput):
    randomletters.insert(userinput,random.choice(fullist))
passwordgenerator()
password = "".join(randomletters)
print(password)