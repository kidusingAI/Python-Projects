print("This is a shopping list created by Ahmed Nakamoto")
item = True
items = []
while item != '':
  item = input("Input an item into your shopping list, if you want to exit to see your items please hit enter")
  if bool(item) == True:
    items.append(item)
  else:
    break
items.sort()
num = len(items)-1
noof = items.count(items[num])
curitem = items[num]
print("Your shopping list includes")
for item in (items):
  print(f"{noof} {curitem}(s)")
  if noof > 1:
    for no in range(noof+1):
      num = num-1
      items.remove(items[num])
    print(curitem)
    print(num)
    print(items.index("b"))
    print(f"{noof} {curitem}(s)")
  noof = items.count(items[num])
  curitem = items[num]
  num = num-1