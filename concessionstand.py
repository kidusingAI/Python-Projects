snacks = {"Popcorn":'1' , "Soda":'2' , "hotdog":'3' , 'corndog':'4'}
order = -5
total = 0
while order != '':
  x = 0
  print("This is a Concession stand, we have ")
  for keys in snacks:
    print(f"{list(snacks.values())[x]}            {list(snacks.keys())[x]}")
    x += 1
  
  order = input("Input the value of the snack you want to order, if you finished ordering and would like to pay please hit enter.")
  
  if order == '1':
    total += 4.5
    print("thnk")
  elif order == '2':
    total += 1.5
  elif order == '3':
    total += 2.5
  elif order == '4':
    total += 3.5

print("-----YOUR TOTAL-----")
print(f"          ${total:6.2f}")
