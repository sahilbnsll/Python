# Types of Inheritance

# Single Inheritance

class Company:
    job = "WEB DEVELOPMENT"
    def showDetails(self):
        print("This is Parent Class")

class Employee(Company):
    language = "Python"
    def getLanguage(self):
        print(f"The Language is {self.language}")

c = Company()
e = Employee()

print(e.job)   # Inheritance Takes Place
