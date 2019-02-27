import random
print("Welcome to the game! Now please think bout a number between 0 and 50. Keep it in mind and the AI will guess your number. After AI answering, you can type in '1', '2', '3' as your answer to let the AI know if the guess is (1) bigger than, (2) smaller than, or (3) equal to your number. ")

guessNum = random.randrange(0,50)
minNum = 0
maxNum = 50

# minNum and maxNum cant work here.

selectedNumList = []
for i in range(100):
    selectedNumList.insert(i, guessNum)
    print("I guess the number is", guessNum)
    userHint = input("Please give a hint to AI: ")

    if int(userHint) == 1:
        guessNum = random.randrange(minNum,guessNum)
        maxNum = max(selectedNumList)
    elif int (userHint) == 2:
        guessNum = random.randrange(guessNum,maxNum)
        minNum = min(selectedNumList)
    elif int(userHint) == 3:
        print("Yay!")
        break
        
if int(userHint) != 3:
    print("I give up!")
