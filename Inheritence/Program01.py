# Basics of Inheritance

class Employee:
    company= "Google Inc."

    def showDetails(self):
        print("This is a employee")


class Programmer(Employee):
    language="Python"
    company= "Youtube"

    def getLanguage(self):
        print(f"The Language is {self.language}")
    
    def showDetails(self):
            print("This is Programmer Class.")


e = Employee()
e.showDetails()
p = Programmer()
p.showDetails()    # Prints same content as e.showDetails because Programmer class doesn't have showDetails() so programmer class inherit showDetails() function from Base class Employee.

print(p.company)   # Prints "Google Inc." as Programmer class doesn't have company, so programmer class inherit company from Base class Employee.

p.showDetails() # Prints "This is Programmer Class" as this time showDetails() is present in Programmer Class.

print(p.company) # Prints "Youtube" as this time company is present in Programmer Class.