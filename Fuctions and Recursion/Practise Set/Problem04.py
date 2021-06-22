# Printing Sum of First n Natural Numbers using Recursion

def sum(n):
    if(n==1):
       return 1
    else:
        return n + sum(n-1)

n=int(input("Enter a natural number: "))
print("the sum of first "+str(n)+" natural numbers is: " +str(sum(n)))