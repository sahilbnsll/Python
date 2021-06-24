# Problem 4. Checking prime number

num=int(input("Enter a Number: "))
prime = True
for i in range(2,num):
    if(num % i == 0):
        prime = False
        break
if prime:
    print("Entered number is prime")
else:
    print("Entered number is not prime")