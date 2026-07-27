x = False
y = 3
def rps():
  global x
  global y
  import random
  k = ['rock','paper','scissors']
  computerchoice = random.choice(k)
  global userchoice
  userchoice = input("Pick your rock,paper or scissors")
  if computerchoice == userchoice:
    print("Its a Draw!")
  elif computerchoice == 'rock' and userchoice == 'paper' or computerchoice == 'scissors' and userchoice == 'rock' or computerchoice == 'paper' and userchoice == 'scissors':
      print("You Win!")
  elif userchoice == 'shoot' and x == False:
      print("Egg of Easter \n Dont do this again!")
      x = True
      y = 1
      return
  if y == 1 and x == True:
        y = 3
        print("I TOLD YOU NOT TO DO IT??!???!!!!!?! NO MORE PLAYING FOR YOU!!!!!!!!!!!!!!!!")
        return
  else:
    print("You lose:(")
rps()
a = True
while a == True and y != 3:
  retry = input("Do you want to play again?")
  if str.lower(retry) == 'yes':
    a = True
    rps()
  elif str.lower(retry) == 'no':
    a = False
    print('Thanks for playing \n Created:Yosef Shamoug')
  else:
    print("It is either Yes or No.")





