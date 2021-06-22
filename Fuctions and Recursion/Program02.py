# Greeting a user 

def greet(name):
    p = print("Good Day, " + name)
    return p

# both approach are correct

greet('Sahil')

name =input("Enter your name: ")
print(greet(name))

