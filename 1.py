import random
#000000
print('Guessing number game')

def play_game():
    # Get bounds inside the function so replayability works perfectly
    lowerbound = int(input("What is the lower bound? "))
    upperbound = int(input("What is the upper bound? "))
    
    # Ensure bounds are valid
    while upperbound <= lowerbound:
        print("Try again. The upper bound must be greater than the lower bound.")
        lowerbound = int(input("What is the lower bound? "))
        upperbound = int(input("What is the upper bound? "))
        
    # Generate the secret number ONCE per game
    # (upperbound + 1 ensures the upper bound itself is included in the choices)
    number = random.randint(lowerbound, upperbound)
    # Loop for guessing
    while True:
        usernumber = int(input("your guess?"))
        if usernumber == number:
            print("Wow, you are Psychic!")
            break  # Exits the guessing loop because they won
        elif usernumber < lowerbound or usernumber > upperbound:
            print("Not in parameters! Stay between your bounds.")
        elif usernumber < number:
            print("Too low")
        elif usernumber > number:
          print("Too high")

# --- Main Game Loop ---
playing = True
while playing:
    play_game()
    
    replay = input("\nInput 1 if you want to replay, or any other key to quit: ")
    if replay != '1':
        playing = True
    else:
      print("Thanks for playing!")
      print("Lead Designer: Ahmed Nakamoto")
