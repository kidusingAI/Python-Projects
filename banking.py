balance = 0
options = input(f"1. Balance\n2. Deposit\n3. Withdraw\nType the number for your option and anything else to quit")

#balance function
def balances():
  print(f"Your balance is currently ${balance:.2f}")

#deposit function
def deposits(deposit):
  while not deposit.replace(".","1").isdigit() or float(deposit) < 0:
    print("Invalid Deposit")
    deposit = input("How much are you going to deposit")
    
  deposit = float(deposit)
  global balance
  balance += deposit
  return balance

#withdrawal function
def withdraws(withdraw):
  global balance
  while not withdraw.replace(".","1").isdigit() or float(withdraw) < 0 or float(withdraw) > balance:
    print("Invalid Withdrawal")
    withdraw = input("How much are you going to withdraw")
    
  withdraw = float(withdraw)
  balance -= withdraw
  return balance

#looping options and function
while options == '1' or options == '2' or options == '3':
  match options:
    case '1':
      print(' ')
      balances()
      options = input(f"1. Balance\n2. Deposit\n3. Withdraw\nType the number for your option and anything else to quit")
    case '2':
      deposits(input("How much are you going to deposit"))
      print(" ")
      balances()
      options = input(f"1. Balance\n2. Deposit\n3. Withdraw\nType the number for your option and anything else to quit")
    case '3':
      withdraws(input("How much are you going to withdraw"))
      print(" ")
      balances()
      options = input(f"1. Balance\n2. Deposit\n3. Withdraw\nType the number for your option and anything else to quit")
print("Session End")
