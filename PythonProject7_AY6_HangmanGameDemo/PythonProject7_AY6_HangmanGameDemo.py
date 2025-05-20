import random

wordList = ["aardvark", "baboon", "camel"]
choosenWord = random.choice(wordList)
numberOfLetter = len(choosenWord)
display = ""
for letter in range(numberOfLetter):
    display += "-"
# print(display)

isPlayerWin = False
isPlayerLoose = False
playerLives = 9

# guessedLetter = input("\nGuess a letter: ").lower()
enteredLetters = []
displayedStr = ""
while(not ((isPlayerWin) or (isPlayerLoose))):
    print(display)
    guessedLetter = input("\nGuess a letter: ").lower()
    if(guessedLetter in enteredLetters):
        print("You already enter this letter.")
        continue
    index = 0
    for letter in choosenWord:
        if(letter == guessedLetter):
            display = list(display)
            display[index] = guessedLetter
            enteredLetters.append(guessedLetter)
        elif (guessedLetter not in choosenWord):
            enteredLetters.append(guessedLetter)
        index += 1
    if("-" not in display):
        isPlayerWin = True
        break
    if(guessedLetter not in choosenWord):
        playerLives -= 1
        if(playerLives <= 0):
            isPlayerLoose = True
            break
    # for letter in display:
    #     displayedStr += letter
    #     display = displayedStr
if(isPlayerWin):
    print("You Win")
elif(isPlayerLoose):
    print("Sorry try again!")

print("***")