# Basics of Inheritance

class Employee:
    company= "Google Inc."

    def showDetails(self):
        print("This is a employee")


class Programmer(Employee):
    language="Python"

    def getLanguage(self):
        print(f"The Language is {self.language}")


e = Employee()
e.showDetails()
p = Programmer()
p.showDetails()    # Prints same content as e.showDetails because Programmer class doesn't have showDetails() so programmer class inherit showDetails() function from Employee class.



