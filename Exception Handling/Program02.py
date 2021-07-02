# Different Exceptions in Python.


try:
    a = int(input("Enter a Number: "))
    c = 1/a
    print(c)

except ValueError as e:
    print("Enter a Valid Input")

except ZeroDivisionError as e:
    print("Make sure you're not dividing by Zero")    



# Add more exceptions-handling statement to this file.
# Thank You.