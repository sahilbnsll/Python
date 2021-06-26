# For Loop in Python
car = ['BMW', 'Bugatti','Mercedes','Audi','Ford','Ferrari']
for item in car:
    print(item)

# range function in python
for i in range(1, 9):
    print(i)

# for loop with else 
for i in range(8):
    print(i)
else:
    print("done")

# break statement
for i in range(9):
    print(i)
    if i ==5:
        break

# continue statement
for i in range(10):
    if i == 5:
        continue #skips the value 5
    print(i)

# pass statement
i =4
if i>0:
    pass #null value
print("Sahil")
