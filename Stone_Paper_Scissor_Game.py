# Rock Paper Scissor Game
import random   # importing ramdom module so that computer can choose random values
def gameWin(comp, you):
    if comp == you:  # When computer and you choose same 
        return None
    elif comp == 's': # checking all posibilities when computer choses stone
        if you == 'p':
            return True
        elif you == 'sc':
            return False
                
    elif comp == 'p': # checking all posibilities when computer choses paper
        if you == 'sc':
            return True
        elif you == 's':
            return False
    elif comp == 'sc': # checking all posibilities when computer choses scissor
        if you == 's':
            return True
        elif you == 'p':
            return False

print("Computer's Turn: Stone(s), Paper(p), Scissor(sc)")
RandNo = random.randint(1,3)
if(RandNo==1):
    comp='s'
elif(RandNo==2):
    comp='p'
elif(RandNo==3):
    comp='sc'
print("Computer has selected")

you=input("Your Turn: Stone(s), Paper(p), Scissor(sc)? ")    

print(f"Computer chose {comp},",end=" ")
print(f"You chose {you}")
result = gameWin(comp, you)

if(result == None):
    print("Game is Tie")
elif result:
    print("Congrats!, You WON")
else:
    print("You Lose")    