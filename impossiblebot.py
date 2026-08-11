import random
print("This is 21 game whoever types the last number loses")
consec = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
y = 0
z = 0

# Removing items from list
def currentlist():
    global consec
    userinput = int(input("How many numbers do you want to remove"))
    while not 4 > userinput >= 1:
        userinput = int(input("invalid input"))
    for i in range(userinput):
        del consec[0]
    print(consec)


def wincondition():
		currentlist()
		global y
		global z
		y = (len(consec)-1)%4
		if y == 0 and len(consec) > 4:
			z = random.randint(1,3)
		elif y != 0 and len(consec) >4:
			z = y
		elif len(consec) <= 4 and len(consec) >1:
			z = len(consec)-1
		elif len(consec) == 1:
			z = 1
		for i in range(z):
			del consec[0]
		print(consec)
		print(f"{len(consec)} numbers left")

while len(consec) >= 0:
    match len(consec):
        case _ if len(consec) == 1:
          currentlist()
          print("I win")
          break
        case _ if len(consec) == 2:
              currentlist()
              del consec[0]
              print("I lose")
              break
        case _ if 2 < len(consec) <= 5:
            wincondition()
        case _ if 5 < len(consec) <= 11:
            wincondition()
        case _ if 11 < len(consec) <= 17:
            wincondition()
        case _ if 17 < len(consec) <= 21:
            wincondition()
