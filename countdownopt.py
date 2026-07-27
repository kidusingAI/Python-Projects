import time
hours = input("Are there hours in your timer? if yes type h")

if hours == 'h':
  hours = int(input("How Many hours do you want"))
else:
  hours = 0

minutes = input("Are there minutes in your timer? if yes type m")

if minutes == 'm':
  minutes = int(input("How Many minutes do you want"))
else:
  minutes = 0

seconds = input("Are there seconds in your timer? if yes type s")

if seconds == 's':
  seconds = int(input("How Many seconds do you want"))
else:
  seconds = 0

total = 3600*hours+60*minutes+seconds

#logic to see how many initial hours minutes and seconds
hours = hours+minutes//60+seconds//3600
minutes = minutes+seconds//60
seconds = seconds%60

#To Prevent negative minutes from printing
if hours >= 0 and minutes >= 0 and seconds >= 0:
  print(f"{hours:02}:{minutes:02}:{seconds:02}")

for x in range(1,total+1,1):
  time.sleep(1)
# Logic to go from 1 hours to 59 minutes and 59 seconds, it is important to write narrow steps before broad ones as to not override your code
  if minutes == 0 and seconds == 0:
    hours = hours-1
    minutes = 59
    seconds = 60
#Logic to go from 1 minute to 59 seconds
  if seconds == 0:
    minutes = minutes-1
    seconds = 59
  else:
    seconds = seconds -1
  

  print(f"{hours:02}:{minutes:02}:{seconds:02}")

print("Times Up!!!")