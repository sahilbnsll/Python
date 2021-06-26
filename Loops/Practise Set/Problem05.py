# Problem 5. sum of first n Natural numbers using while loop.

num=int(input("Enter a Number: "))
sum = 0 
while num > 0:
   sum = sum + num
   num = num-1
print(f"Sum of first {num} number is {sum}")