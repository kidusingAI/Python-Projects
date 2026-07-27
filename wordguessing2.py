#A guessing game of names
import random
def game():
#defining parameters of names and the name chosen whilst defining the number of attempts to use to understand how many hints to give players
    names = [
    "Liam", "Olivia", "Noah", "Emma", "Oliver", "Ava", "Elijah", "Charlotte", "William", "Sophia",
    "James", "Amelia", "Benjamin", "Isabella", "Lucas", "Mia", "Henry", "Evelyn", "Alexander", "Harper",
    "Mason", "Camila", "Michael", "Gianna", "Ethan", "Abigail", "Daniel", "Luna", "Jacob", "Ella",
    "Logan", "Elizabeth", "Jackson", "Sofia", "Levi", "Avery", "Sebastian", "Scarlett", "Mateo", "Eleanor",
    "Jack", "Madison", "Owen", "Layla", "Theodore", "Penelope", "Aiden", "Aria", "Samuel", "Chloe",
    "Joseph", "Grace", "John", "Ellie", "David", "Nora", "Wyatt", "Hazel", "Matthew", "Zoey",
    "Luke", "Riley", "Asher", "Victoria", "Carter", "Lily", "Julian", "Aurora", "Santiago", "Violet",
    "Grayson", "Nova", "Leo", "Hannah", "Jayden", "Emilia", "Gabriel", "Zoe", "Isaac", "Stella",
    "Lincoln", "Stella", "Anthony", "Everly", "Hudson", "Isla", "Dylan", "Leah", "Ezra", "Lillian",
    "Thomas", "Addison", "Charles", "Willow", "Christopher", "Lucy", "Jaxon", "Paisley", "Maverick", "Natalie"
]
    compans = random.choice(names)
    print("what is your first guess")
    attempts = 0
    while True:
#loop of guesses till answer reached or player loses, progressively more hints
        attempts += 1
        userinput = input()
        if userinput.lower() == compans.lower():
            print("You got it!")
            break
            
        elif userinput.lower() != compans.lower() and attempts == 1:
            print("The name has",len(compans),"letters")
            print("What is your next guess")
            
        elif userinput.lower() != compans.lower() and attempts > 1 and attempts <= len(compans):
            print("The",attempts-1,"letter is",compans[attempts-2])
            print("Next guess?")
            
        else:
            print("You failed Haha!")
            print("The answer was", compans)
            break
            return
game()
print("")
print("Want to try again, Press enter to retry press emter any other character to not.")
retry = input()
while retry == '':
    game()
