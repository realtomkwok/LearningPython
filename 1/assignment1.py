import random

minNum = 1
maxNum = 50

print("Welcome to the game! Now please think bout a number between 0 and 50. Keep it in mind and the AI will guess your number. After AI answering, you can type in '1', '2', '3' as your answer to let the AI know if the guess is (1) bigger than, (2) smaller than, or (3) equal to your number. ")

for i in range(5):
    guessNum = random.randrange(minNum,maxNum)
    print(f"I guess the number is {guessNum}")
    userHint = int(input("Am I right? "))

    if userHint == 1: #guessNum is greater than userNum
        maxNum = guessNum-1
    elif userHint == 2: #guessNum is smaller than userNum
        minNum = guessNum+1
    elif userHint == 3: #guessNum is equal to userNum
        print(f"Yay! So the number is {guessNum}.")
        break
    
if userHint != 3:
    print("Alright, I give up!")
    
