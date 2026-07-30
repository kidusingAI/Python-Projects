import random
slot_choices = ['🍒']
balance = 1000
#Amountt of bet
def bet():
  global amtbet
  global balance
  amtbet=input("How much do you want to bet")
  while not amtbet.replace('.','1').isdigit() or float(amtbet) < 0 or float(amtbet) > balance:
    print("Invalid Choice")
    amtbet = input("How much do you want to bet?")
  float(amtbet)
  balance -= float(amtbet)
  return amtbet,balance

# Random choices
def choices():
  global choice
  choice = [random.choice(slot_choices) for _ in range(3)]

#how much you win
def payout():
  global win
  global amtbet
  global balance
  print("********")
  for i in range(3):
    print(choice[i],end = "")
  print(" ")
  print("********")
  if len(set(choice)) > 1:
    print("Haha Loser No Payout!!! House Always wins! call 1(800)-Gambler")
    print(f"Your current balance is ${balance:.2f}")
  else:
    amtbet = float(amtbet)
    match choice[0]:
      case '🍒':
        amtbet *= 20
        win = amtbet-(amtbet/20)
        print(f"You win ${win:.2f} profit. Leave now!!!")
        balance += win
        return balance
      case '🍉':
        amtbet *= 10
        win = amtbet-(amtbet/10)
        print(f"You win ${win:.2f} profit. Leave now!!!")
        balance += win
        return balance
      case '🍓':
        amtbet *= 5
        win = amtbet-(amtbet/5)
        print(f"You win ${win:.2f} profit. Leave now!!!")
        balance += win
        return balance
      case '🥭':
        amtbet *= 2.5
        win = amtbet-(amtbet/2.5)
        print(f"You win ${win:.2f} profit. Leave now!!!")
        balance += win
        return balance
      case '🍌':
        amtbet *= 1.25
        win = amtbet-(amtbet/1.25)
        print(f"You win ${win:.2f} profit. Leave now!!!")
        balance += win
        return balance

while input(f" \n Your Current Balance is ${balance}\nDo you want to spin the machine?(y/n)").lower() == 'y':
    bet()
    print(f"Bet is set. You are betting ${amtbet}")
    choices()
    payout()

print("You either got scammed or never played!")
