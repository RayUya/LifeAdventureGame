print ("---- WELCOME TO MY QUIZ GAME ----")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! let's play ")
score = 0

answer = input("What does ATM stands for? ")
if answer.lower() == "Automated Teller Machine":
        print('Correct!')
        score += 1

else:
    print("Incorrect!")

answer = input("What does AI stands for? ")
if answer.lower() == "Artificial Intelligence":
        print('Correct!')
        score += 1
else:
        print("Incorrect!")

answer = input("What does PDA stands for? ")
if answer.lower() == "Public Display of Affection ":
        print('Correct!')
        score += 1
else:
        print("Incorrect!")

answer = input("What does RAM stands for? ")
if answer.lower() == "Random Access Memory":
        print('Correct!')
        score += 1
else:
        print("Incorrect!")

        print("You got " + str(score) + " questions correct")
        print("You got " + str((score/4) * 100) + "%.")