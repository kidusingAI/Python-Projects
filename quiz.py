questions = ("Who discovered relativity?","What year did Niel Armstrong land on the moon","who was the first person in space")
A = ("Isaac Newton","1969","Niel Armstrong")
B = ("Albert Einstein","1968","Buzz Aldrin")
C = ("Nicola Tesla","1970","Yuri Gagarin")
D = ("Erwin Schrödinger","1967","Michael Collins")
answers = ('b','a','c')
x = 0
points = 0
for question in questions:
  print(question)
  print(f"A.{A[x]}\nB.{B[x]}\nC.{C[x]}\n{D[x]}")
  selection = input("select A,B,C or D as your answer to lock it in")
  if answers[x] == selection.lower():
    print("You Got it Right!!!")
    print(" ")
    print(" ")
    print(" ")
    points += 1
  else:
    print("You got it wrong. :( Better Luck Next Time!")
    print(" ")
    print(" ")
    print(" ")
  x+= 1
  
print("-----YOUR SCORE-----")
print(f"{points}/3")
  
