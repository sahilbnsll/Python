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



# Multiple Inheritance

class Employee:
    company = "Visa"
    ecode = 207

class Freelancer:
    company = "Fiverr"
    level = 0
    def upgradeLevel(self):
        self.level = self.level + 1
        

class Programmer(Employee,Freelancer):   # here Employee class is inherit first so its properties have priority
    name = "Sahil"

p = Programmer()
p.upgradeLevel()
print(p.level)
print(p.ecode)
print(p.company)



# Multi-Level Inheritance

class Person:
    country = "India"

    def takeBreath(self):
        print("I'm Breathing...")

class Employee(Person):
    company = "Audi"
    name = "Sahil"

    def getSalary(self):
        print(f"Salary is {self.salary}")

    def takeBreath(self):
        print(f"I'm {self.name} & I'm also Breathing...")

class Programmer(Employee):
    company = "BMW"
    def getSalary(self):
        print("No Salary for Programmer")


p = Person()
p.takeBreath()
e = Employee()
pr = Programmer()
pr.takeBreath()
print(pr.company)
print(pr.country)

