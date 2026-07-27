x = 0
shoppinglist = []
while x != '':
  shopping = input("this is a shopping list, if you would like to put an item in the list please do so here \n if you want to exit please hit enter")
  x = shopping
  if x == '':
    break
  shoppinglist.append(shopping)
  print(shoppinglist)
shoppinglist = shoppinglist
num = 0
item = shoppinglist[num-2]
print("You Have:")
for z in range(len(set(shoppinglist))):
  print(shoppinglist.count(item),' ',item)
  iis = shoppinglist.count(item)
  if shoppinglist.count(item) > 1:
   for duplicates in range(iis):
     shoppinglist.pop(iis-1)
     iis = iis-1
  num = len(shoppinglist)-1
  item = shoppinglist[num]