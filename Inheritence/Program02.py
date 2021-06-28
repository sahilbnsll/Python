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