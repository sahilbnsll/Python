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


