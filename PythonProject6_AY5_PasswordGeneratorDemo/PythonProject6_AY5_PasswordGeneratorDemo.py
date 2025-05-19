import random

lowerCaseLetters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upperCaseLetters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to PyPassword Generator!")
numberLowerCaseLetters = int(input("How many lower case letters would you like in your password?\n"))
numberUpperCaseLetters = int(input("How many upper case letters would you like in your password?\n"))
numberOfNumbers = int(input("How many numbers would you like in your password?\n"))
numberOfSymbols = int(input("How many symbols would you like in your password?\n"))

choosenPasswordItems = []
choosenLowerCaseLetters = []
choosenUpperCaseLetters = []
choosenNumbers = []
choosenSymbols = []
mixedPasswordItems = []

# Easy way - Unmixed Password

i = 0
while (i < numberLowerCaseLetters):
    choosenLowerCaseItem = random.choice(lowerCaseLetters)
    choosenLowerCaseLetters.append(choosenLowerCaseItem)
    choosenPasswordItems.append(choosenLowerCaseItem)
    i = i + 1

i = 0
while (i < numberUpperCaseLetters):
    choosenUpperCaseItem = random.choice(upperCaseLetters)
    choosenUpperCaseLetters.append(choosenUpperCaseItem)
    choosenPasswordItems.append(choosenUpperCaseItem)
    i = i + 1

i = 0
while (i < numberOfNumbers):
    choosenNumberItem = random.choice(numbers)
    choosenNumbers.append(choosenNumberItem)
    choosenPasswordItems.append(choosenNumberItem)
    i = i + 1

i = 0
while (i < numberOfSymbols):
    choosenSymbolItem = random.choice(symbols)
    choosenSymbols.append(choosenSymbolItem)
    choosenPasswordItems.append(choosenSymbolItem)
    i = i + 1

# choosenPasswordItems.append(choosenLowerCaseLetters)
# choosenPasswordItems.append(choosenUpperCaseLetters)
# choosenPasswordItems.append(choosenNumbers)
# choosenPasswordItems.append(choosenSymbols)
print(choosenPasswordItems)

# Hard way - Mixed Password

random.shuffle(choosenPasswordItems)
mixedPasswordItems = ""
for item in choosenPasswordItems:
    mixedPasswordItems += item

print(mixedPasswordItems)

# Harder way - Mixed Password (No duplicate allowed!)
choosenSetPasswordItems = set({})
choosenSetLowerCaseLetters = set({})
choosenSetUpperCaseLetters = set({})
choosenSetNumbers = set({})
choosenSetSymbols = set({})
mixedSetPasswordItems = set({})


while (len(choosenSetLowerCaseLetters) < numberLowerCaseLetters):
    choosenLowerCaseItem = random.choice(lowerCaseLetters)
    choosenSetLowerCaseLetters.add(choosenLowerCaseItem)
    choosenSetPasswordItems.add(choosenLowerCaseItem)
    i = i + 1

i = 0
while (len(choosenSetUpperCaseLetters) < numberUpperCaseLetters):
    choosenUpperCaseItem = random.choice(upperCaseLetters)
    choosenSetUpperCaseLetters.add(choosenUpperCaseItem)
    choosenSetPasswordItems.add(choosenUpperCaseItem)
    i = i + 1

i = 0
while (len(choosenSetNumbers) < numberOfNumbers):
    choosenNumberItem = random.choice(numbers)
    choosenSetNumbers.add(choosenNumberItem)
    choosenSetPasswordItems.add(choosenNumberItem)
    i = i + 1

i = 0
while (len(choosenSetSymbols) < numberOfSymbols):
    choosenSymbolItem = random.choice(symbols)
    choosenSetSymbols.add(choosenSymbolItem)
    choosenSetPasswordItems.add(choosenSymbolItem)
    i = i + 1

print(choosenSetPasswordItems)
