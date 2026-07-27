global answer
global onenumop
import math
print("Calculator \n By Yosef Shamoug")
operations = math.ceil(float(input("How many operations do you want")))
x = 0
answer = 0
onenumop = 0
for x in range(operations):
  typeofoperation = input("what type of operations do you want \n division(/) multiplication(*),addition(+) subtraction(-) \n Square Root(sqrt)  or absolute value(abs)")
#this is for addition
  if typeofoperation == '+':
    firstnumber = input("What is the first number you want to add, if it is the previous answer type ans")
    secondnumber  = input("What is the second number you want to add, if it is the previous answer type ans")
    
    if firstnumber == 'ans':
      answer = float(answer)+float(secondnumber)
    elif secondnumber == 'ans':
      answer = float(firstnumber)+float(answer)
    elif firstnumber != 'ans' or secondnumber != 'ans':
      answer = float(firstnumber)+float(secondnumber)

#this is for subtraction
  if typeofoperation == '-':
    firstnumber = (input("What is the number you want to subtract, if it is the previous answer type ans"))
    secondnumber  = (input("What is the number you want to subtract by, if it is the previous answer type ans"))
    
    if firstnumber == 'ans':
      answer = float(answer)-float(secondnumber)
    elif secondnumber == 'ans':
      answer = float(firstnumber)-float(answer)
    else:
      answer = float(firstnumber)-float(secondnumber)

#this is for multiplication
  if typeofoperation == '*':
    firstnumber = (input("What is the first number you want to multiply, if it is the previous answer type ans"))
    secondnumber  = (input("What is the second number you want to multiply, if it is the previous answer type ans"))
    
    if firstnumber == 'ans':
      answer = float(answer)*float(secondnumber)
    elif secondnumber == 'ans':
      answer = float(firstnumber)*float(answer)
    else:
      answer = float(firstnumber)*float(secondnumber)
      
#this is for division
  if typeofoperation == '/':
    firstnumber = (input("What is the number you want to divide, if it is the previous answer type ans"))
    secondnumber  = (input("What is the number you want to divide by, if it is the previous answer type ans"))
    
    if firstnumber == 'ans':
      answer = float(answer)/float(secondnumber)
    elif secondnumber == 'ans':
      answer = float(firstnumber)/float(answer)
    else:
      answer = float(firstnumber)/float(secondnumber)

#this is for square root
  if typeofoperation == 'sqrt':
   onenumop = input("what is the number you want to squareroot if it is the previous answer type ans")
  if onenumop == 'ans' and typeofoperation == 'sqrt':
     answer = math.sqrt(answer)
  elif onenumop != 'ans' and typeofoperation == 'sqrt':
      answer = math.sqrt(float(onenumop))

#this is for absolute value
  if typeofoperation == 'abs':
   onenumop = input("what is the number you want to find the absolute value of if it is the previous answer type ans")
  if onenumop == 'ans' and typeofoperation == 'abs':
     answer = abs(answer)
  elif onenumop != 'ans' and typeofoperation == 'abs':
      answer = abs(float(onenumop))
  if int(answer) == answer:
    print(int(answer))
  else:
    print(answer)