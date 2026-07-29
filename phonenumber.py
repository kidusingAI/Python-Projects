#to create a phone number

def phonenumber(countrycode,areacode,first3,last3):
  print(f"+{countrycode}({areacode}) {first3}-{last3}")

phonenumber(countrycode=1,areacode=234,first3=567,last3=890)
