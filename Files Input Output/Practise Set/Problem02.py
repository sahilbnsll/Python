import random
randNo = random.randint(1,10000)

def game():
    return randNo

score = game()
with open('problem02.txt') as f:
    highScore =f.read()

if highScore =='':
    with open('problem02.txt', 'w') as f:
        f.write(str(score))

elif int(highScore)<score :
    with open('problem02.txt', 'w') as f:
        f.write(str(score))

print(f"Your Score is: {randNo}")

if int(score)<int(highScore) :
    print(f"Sorry, you failed to break the highscore: {str(highScore)}")

elif int(score)>int(highScore) :
    print(f"Congrats!, You created a Highscore")
    print(f"Updated HighScore is: {randNo}")

print(f"Previous Highscore is: {str(highScore)}")    


