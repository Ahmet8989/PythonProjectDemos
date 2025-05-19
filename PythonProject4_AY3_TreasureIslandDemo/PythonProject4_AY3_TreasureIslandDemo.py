print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choiceOne = input("You're at a crossroad, where do you want to go? Type \"left\" or \"right\".").lower()
if (choiceOne == "right"):
    print("You fell in to a hole. Game over!")
elif (choiceOne == "left"):
    print("You've come to a lake, there is an island in the middle of the lake.")
    choiceTwo = input("Type \"wait\" to wait for a boat. Type \"swim\" to swim across.").lower()
    if(choiceTwo == "wait"):
        print("You arrive to the island unharmed. There is house with three doors.")
        choiceThree = input("One red, one yellow, and one blue. Which color do you choose?").lower()
        if(choiceThree == "red"):
            print("It's a room full of fire. Game Over!")
        elif(choiceThree == "yellow"):
            print("You found the treasure. You Win!")
        elif(choiceThree == "blue"):
            print("It's a room full of water. Game Over!")
        else:
            print("You enter an invalid option.")
    elif(choiceTwo == "swim"):
        print("You got attacked by piranha. Game over!")
    else:
        print("You enter an invalid option.")
else:
    print("You enter an invalid option.")
