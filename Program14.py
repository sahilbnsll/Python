# # while Loop
# i = 0
# while i<10:
#     print("Yes " + str(i))
#     i= i + 1

# print("done!")

# # quick example

# from typing import Container


# a=1
# while a<=50:
#     print(a)
#     a = a+1

# print("Done!")

# # example- Priniting content of a list 
# car = ['BMW', 'Bugatti','Mercedes','Audi','Ford','Ferrari']
# i=0
# while i<len(car):
#     print(car[i])
#     i=i+1
# print("Done!")    

# # above example using for loop
# car = ['BMW', 'Bugatti','Mercedes','Audi','Ford','Ferrari']
# for item in car:
#     print(item)

# # range function in python
# for i in range(1, 9):
#     print(i)

# # for loop with else 
# for i in range(8):
#     print(i)
# else:
#     print("done")

# # break statement
# for i in range(9):
#     print(i)
#     if i ==5:
#         break

# # continue statement
# for i in range(10):
#     if i == 5:
#         continue #skips the value 5
#     print(i)

# # pass statement
# i =4
# if i>0:
#     pass #null value
# print("Sahil")


# # Problem 1. Multiplication Table

# i=1
# num=int(input("Enter a number: "))
# for i in range(1,11):
#     print(str(num)+" X "+str(i)+" = "+str(num*i))
#     #print(f"{num} X {i} = {num*i}") #same as above


# # Problem 2. Name starts with s in list 

# l=["Sahil","Sooraj","Dhruv","Kshitij","Mukul"]
# for name in l:
#     if name.startswith("S"):
#         print("Hello " + name)


# # Problem 3. Problem 1 in while loop 

# i=1
# num=int(input("Enter a Number: "))
# while i<=10:
#     print(f"{num} X {i} = {num*i}")
#     i=i+1


# # Problem 4. Checking prime number

# num=int(input("Enter a Number: "))
# prime = True
# for i in range(2,num):
#     if(num % i == 0):
#         prime = False
#         break
# if prime:
#     print("Entered number is prime")
# else:
#     print("Entered number is not prime")

# # Problem 5. sum of first n Natural numbers using while loop

# num=int(input("Enter a Number: "))
# sum = 0 
# while num > 0:
#    sum = sum + num
#    num = num-1
# print(f"Sum of first {num} number is {sum}")  

# # Problem 6. factorial of number

# num=int(input("Enter a Number: "))
# fact = 1
# for i in range(1, num+1):
#    fact = fact*i
# print(f"Factorial of number {num} is {fact}")   

# # # Problem 7. Star Pattern *
# #                           **
# #                           ***

# num=int(input("Enter a Number: "))
# for i in range(num+1):
#     print("*" *i)


# # # Problem 8. Star Pattern  *
# #                           ***
# #                          *****

# num=int(input("Enter a Number: "))
# for i in range(num):
#     print(" " * (num-i-1),end="")
#     print("*" * (2*i+1),end="")
#     print(" " * (num-i-1))


# # Problem 9. Write a program to print the following star pattern: * * *
#                                     #                             *   *             
#                                              #                    * * * 

# n=3   #int(input("Enter a Number: "))
# for i in range(n+1):
#     print("x" * (n-2*i),end="")
#     print(" " *(2*i-1),end="")
#     print("x" * (n+2*i-3-i))


