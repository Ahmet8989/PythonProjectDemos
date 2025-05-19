import random

rock = "rock"
paper = "paper"
scissor = "scissor"
options = [rock, paper, scissor]

choosenIndexByPlayer = int(input("What do you choose? Type 0 for Rock, 1 for paper or 2 for scissors."))
while(not((choosenIndexByPlayer == 0) or (choosenIndexByPlayer == 1) or (choosenIndexByPlayer == 2))):
    choosenIndexByPlayer = int(input("What do you choose? Type 0 for Rock, 1 for paper or 2 for scissors."))
print()

choosenByPlayer = options[choosenIndexByPlayer]
choosenByComputer = random.choice(options)

print(choosenByPlayer)
print("Computer choose: ")
print(choosenByComputer)

if((choosenByPlayer == rock) and (choosenByComputer == paper)):
    print("You loose!")
elif((choosenByPlayer == rock) and (choosenByComputer == scissor)):
    print("You Win!")
elif((choosenByPlayer == scissor) and (choosenByComputer == paper)):
    print("You Win!")
elif((choosenByPlayer == scissor) and (choosenByComputer == rock)):
    print("You loose!")
elif((choosenByPlayer == paper) and (choosenByComputer == rock)):
    print("You Win!")
elif((choosenByPlayer == paper) and (choosenByComputer == scissor)):
    print("You loose!")
elif():
    print("It's a draw.")
else:
    print("Something went wrong.")
print("***")
