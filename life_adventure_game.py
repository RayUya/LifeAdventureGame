name =  input("Type your Name: ")
print("Welcome", name, "to this adventure")

answer = input(
    "You are stuck in between life. "
    "Choose your destination? (wealth/impact) ").lower()

if answer == "wealth":
    answer = input("You have earned a gold bar for cash. "
                   "Type c to change and k to keep: ")

    if answer == "c":
        print("You have successfully earned $1.")
    elif answer == "k":
        print("You have kept your gold bar.")
    else:
        print('Not a valid choice. You loose')

elif answer == "impact":
    answer = input("You have earned a Certificate."
                   "Do you want to use it or keep it? (use/keep)")

    if answer == "use":
        print("You are now a tool used to impact humanity")
    elif answer == "keep":
        answer = input("Your knowledge will become unaffected."
                       "Do you want to change your mind?(yes/no)")

        if answer == "yes":
            print("The faintest ink is faster that the sharpest memory"
                  "You now have a chance to impact humanity")
        elif answer == "no":
            print("You have lost")
        else:
            print('Not a valid choice. You loose')
    else:
        print('Not a valid choice. You loose')

else:
    print('Not a valid choice. You loose')

    print("Thank you for playing", name)

