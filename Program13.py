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
else:     ##else is optional in program. if we don't make else and if or elif both conditions not satisfy then will not run
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


# 'is' and 'in' in python

s = None
if(s is None):
    print("Yes")
else:
    print("NO")

b = [45,76,24,90,12]
print(45 in b)  # Returns True or False Values

# Problem 1. greatest of four number entered by user

num1 = int(input("Enter Number 1: "))
num2 = int(input("Enter Number 2: "))
num3 = int(input("Enter Number 3: "))
num4 = int(input("Enter Number 4: "))

if(num1>num2):
    f1 = num1
else:
    f1 = num2    

if(num3>num4):
    f2 = num3
else:
    f2 = num4

if(f1>f2):
    print(f1, "is Greatest")
else:
    print(f2, "is Greatest")    


# problem 2. student pass or fail

sub1 = int(input("Enter marks in subject 1:"))
sub2 = int(input("Enter marks in subject 2:"))
sub3 = int(input("Enter marks in subject 3:"))
total=(sub1+sub2+sub3)/3
if(sub1<33 or sub2<33 or sub3<33):
    print("You are Fail because you have less than 33% in one of the subjects")
elif(total<40):
    print("You are Fail because you don't pass the criteria of 40%")
else:
    print("Congratulations!, You Passed the exam")    

# Problem 3. Spam detect
text = input("Enter a Text Message:\n")
spam = False
if("make a lot of money" in text):
    spam = True
elif("click this" in text):
    spam = True
elif("buy now" in  text):
    spam = True
elif("subscribe this" in text):
    spam = True

if(spam):
    print("This text is SPAM") 
else:
    print("This text is not SPAM")


# Problem 4. username is greater than 10 characters or not

username = input("Enter your Username:\n")
lenght = len(username)
if(lenght == 10):
    print("Username", username,"is Correct")
else:
    print("Username is not Correct")    


# Problem 5. name is present in list or not

mylist = ["sahil","dhruv","kshitij","mukul","abhay","ankush","anurag","ayush"]
myname = input("Enter a Name:\n")
if(myname in mylist):
    print(myname, "is present in my List")
else:
    print(myname, "is not present in my List")    

# Problem 6. Student grades

mark = int(input("Enter your marks: "))

if(mark >= 90):
    print("Your grade is O")
elif (mark >= 80):
    print("Your grade is A")
elif (mark >= 70):
    print("Your grade is B")
elif (mark >= 60):
    print("Your grade is C")
elif (mark >= 50):
    print("Your grade is D")
else :
    print("Your grade is F")
    