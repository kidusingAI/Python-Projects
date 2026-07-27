username = input("What is your username")
if username.count(" ") > 0:
  print("Username Cannot Contain Spaces.")
  
elif len(username) > 12:
  print("Username Cannot Contain more than 12 characters")
  
elif not username.isalpha():
  print("Username Cannot Contain any digits")
  
else:
  print("Username is Valid")