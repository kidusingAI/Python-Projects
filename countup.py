#Another one IK
import time
def countup(startno=0,interval=1,):
  length = input("how long do you want the timer in seconds")
  if not length.isdigit():
    length = input("how long do you want the timer in seconds")
  else:
    length = int(length)
    for amtime in range(length):
      startno+=interval
      time.sleep(interval)
      print(startno)
    print("Time's up!")
countup()
  
