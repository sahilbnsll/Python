# The Perfect Guess Game

import random
RandNo= random.randint(1,100)
print(RandNo)
userGuess = None
guesses = 0

while(userGuess != RandNo):
    userGuess = int(input("Enter your guess: "))
    guesses += 1
    if userGuess == RandNo:
        print("Congratulations!, You guessed it right.\n")
    else:
        if(userGuess > RandNo):
            print("You guessed it wrong. Enter a smaller number.\n")
        else:
            print("You guessed it wrong. Enter a larger number.\n")        
    
with open('highScore.txt', 'r') as f:
    highScore =int(f.read())

if(guesses < highScore):
    print("Congrats!, You just broken a HighScore!")
    with open("highScore.txt","w") as f:
        highScore = f.write(str(guesses))
elif(guesses == highScore):
    print("You just tie a HighScore")        

print(f"You guessed the number in {guesses} guesses.")
print(f"The Current HighScore is {highScore}.")

