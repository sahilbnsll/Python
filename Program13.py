a = 50

# 1. if-elif-else Ladder in Python
if(a>5):
    print("Value of a is Greater than 5")    
elif(a>15):
    print("Value of a is Greater than 15")
elif(a>25):
    print("Value of a is Greater than 25")
elif(a>35):
    print("Value of a is Greater than 35")
else:
    print("Value of a is not Greater than 5,15,25,35")


# 2. Mutliple if Statements
if(a<9):
    print("Value of a is lesser than 9")
if(a>24):
    print("Value of a is Greater than 24")
if(a>43):
    print("Value of a is Greater than 43")
else:
    print("Value is not Greater")


# if-else example


age=int(input("Enter your Age: "))
if(age>=18):
    print("Yes, You're an adult")
else:
    print("Sorry, you're not an adult")    
   
#  Logical and relational operators in conditional statements
  
myAge=int(input("Enter your Age: "))
if(myAge>=18 and myAge<=60):
    print("You're eligible to work with us")
else:
    print("You can't work with us")

if(myAge>60 or myAge<60):
    print("You're eligible")
else:
    print("You're not eligible")        