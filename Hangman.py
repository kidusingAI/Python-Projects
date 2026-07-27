from collections import Counter
x = list("adam")
print("This is Hangman a game made by Yosef Shamoug\n","The word you are to guess has",len(x),"letters")
userinput = input("_ "*len(x))
userlist = list(userinput.casefold())
counterx = Counter(x)
counteruserinput = Counter(userlist)
allintersections = counterx & counteruserinput
y = list(allintersections.elements())
lengthy = len(y)
sety = set(y)
len(Counter(y))
z = 0
for index, letters in enumerate(sety):
  checkstep = y.count(letters)
  if checkstep > 0 :
    m = x.append('a')
    print(m)
    z = z+checkstep