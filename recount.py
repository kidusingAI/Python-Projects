import time
hours = input("Would you like to input hours if so type h")
if hours.lower() == "h":
  hours = int(input("How many hours would you like"))
else:
  hours = 0

minutes = input("Would you like to input minutes if so type m")
if minutes.lower() == 'm':
  minutes = int(input("How many minutes would you like"))
else:
  minutes = 0

seconds = input("Would you like to input seconds if so type s")
if seconds.lower() == 's':
  seconds = int(input("How many seconds would you like"))
else:
  seconds = 0
  
total = 3600*hours+60*minutes+seconds

for x in reversed(range(total)):
  hours = x//3600
  minutes = (x-3600*hours)//60
  seconds = x-3600*hours-60*minutes+1

  if seconds >= 60:
    minutes = minutes+1
    seconds = seconds-60
  
  if minutes >= 60:
    hours = hours + 1
    minutes = minutes -60
  
  print(f"{hours:02}:{minutes:02}:{seconds:02}")
  time.sleep(1)
print("TIME IS UP!!!!!!!!!!!!!!")