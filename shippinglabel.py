#Create a shipping label
def shipping_label(*args,**kwargs):
  for arg in args:
    print(arg, end = ' ')
  print(" ")
  print(f"{kwargs.get('street')}\n{kwargs.get("city")} Apartment Number {kwargs.get('apt')}\n {kwargs.get("state")} {kwargs.get('zipcode')}")
shipping_label(
               "Mr."
               ,"Yosef"
               ,"Muhammad"
               ,"III"
               ,street= '123 fake street'
               ,apt = '24-04'
               ,city = 'New York City'
               ,state = "New York"
               ,zipcode = 123456
               )
