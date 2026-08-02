import random
def reset():
  global guess
  global winstring
  global display_show
  global attempts
  global words
  global display
  global hangword
  global word
  word = [
         'apple',
         'pineapple',
         'mango',
         'pear',
         'peach'
         ]
  guess = ''
  hangword = random.choice(word)
  display = ['-']*len(hangword)
  display_show = ' '.join(display)
  winstring = ''.join(display)
  attempts = 0
replay = 'y'
def add_letter():
  global guess
  global winstring
  global display_show
  global attempts
  for i in range(len(hangword)):
    if guess in hangword and hangword[i] == guess:
      display[i] = guess
      display_show = ' '.join(display)
      winstring = ''.join(display)
    if guess not in hangword:
      attempts += 1
      guess = input("Guess a letter")
      if guess in hangword and hangword[i] == guess:
        display[i] = guess
        display_show = ' '.join(display)
        winstring = ''.join(display)
        print(display_show)
  if winstring == hangword and attempts <6:
    print("You win!")
    return
  elif winstring != hangword and attempts > 6:
    print('You lose')
    return
  return display_show


if __name__ == '__main__':
  reset()
  while winstring != hangword:
    winstring = ''.join(display)
    print(display_show)
    guess = input("Guess a letter")
    add_letter()
  replay = input("Do you want to replay this.(y/n)").lower()
reset()
while replay == 'y':
  winstring = ''.join(display)
  print(display_show)
  guess = input("Guess a letter")
  add_letter()
  if winstring == hangword:
    replay = input("Do you want to replay this.(y/n)").lower()
print("Thank you for playing!!!")
