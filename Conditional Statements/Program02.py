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
