import time
global z
h = 0
m = 0
s = 0
z = 0
amtoftime = input("do you want to input hours? If yes type h. If not type anything else")

if amtoftime == 'h':
  h = int(input("how many hours do you want"))
  amtoftime = input("do you want to input minutes? If yes type m. If not type anything else")
  if amtoftime != 'm':
      s = int(input('how many seconds do you want?'))
      z = 2
  if amtoftime == 'm':
    m = int(input('how many minutes do you want to put in m'))
    amtoftime = input("do you want to input seconds? If yes type s. If not type anything else")
  if amtoftime == 's' and z != 2:
    s = int(input('how many seconds do you want?'))
    z = 1
elif amtoftime != 'h':
  amtoftime = input("do you want to input minutes? If yes type m. If not type anything else")
  if amtoftime != 'm':
      s = int(input('how many seconds do you want?'))
      z = 1
  if amtoftime == 'm':
    m = int(input('how many minutes do you want to put in m'))
    amtoftime = input("do you want to input seconds? If yes type s. If not type anything else")
  if amtoftime == 's' and z != 1:
    s = int(input('how many seconds do you want?'))

print("The timer is set")
x = 1
y = 3600*h+60*m+s
minsleft = 0
secondsleft = 0
hrsleft = 0
while x <= 3600*h+60*m+s:
  hrsleft = int(y/3600)
  if hrsleft >= 1:
    minsleft = int((y%3600)/60)
    if minsleft >= 1:
      secondsleft = (y%3600)%60
  if hrsleft == 0:
    minsleft = int(y/60)
    secondsleft = y%60
  print(f"You have {hrsleft} hours {minsleft:02} Minutes and {secondsleft:02} Seconds left")
  time.sleep(1)
  y = y-1
  x = x+1
print("TIME IS UP!!!!!!!!!!!!!!")