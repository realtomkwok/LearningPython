import random
print("Welcome to the game! Now please think bout a number between 0 and 50. Keep it in mind and our AI will guess your number. After AI answering, you can type inYou can type in '1', '2', '3' as your answer to let the program know if the guess is (1) bigger than, (2) smaller than, or (3) equal to your number. ")

for i in range(5):
    guess = random.randrange(0,50)
    print(guess)
    x = input("Please give a hint to AI: ")
    
    if int(x) == 1:
        guess = random.randrange(guess,50)
    if int (x) == 2:
        guess = random.randrange(0,guess)
    if int(x) == 3:
        print("Yay!")
        break
        
if guess != x:
    print("I give up ugh!")
