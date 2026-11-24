# Description: Prompts user to enter 15 numbers into a list, then loops through
#              the list to evaluate and display if each number is even or odd.

# Constant declaration
TOTAL_NUMBERS = 15      # Total count of numbers collected from user

# Variable declarations
numberList = []         # List storing the 15 integer values entered by user
index = 0               # Loop control counter for collecting user inputs
userInput = 0           # Integer value entered by user on each prompt
currentNumber = 0       # Current list evaluated in the even or odd loop

# Definite loop to collect 15 numbers and append them to list
for index in range(TOTAL_NUMBERS):
    userInput = int(input("Enter number #" + str(index + 1) + ": "))
    numberList.append(userInput)

print()                 # Blank line separating input prompts from output results

# Loop through list to determine and display if each number is even or odd
for currentNumber in numberList:
    if (currentNumber % 2 == 0):
        print(str(currentNumber) + " is even")
    else:
        print(str(currentNumber) + " is odd")
