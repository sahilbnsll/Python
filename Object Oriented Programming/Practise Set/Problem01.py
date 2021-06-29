# Problem 1. Creating a Class for storing information for other Programmers.

class Programmer:
    company = "Microsoft Corporation"
    def __init__(self, name, salary,product):
        self.name = name
        self.salary = salary
        self.product = product

    def getInfo(self):
        print(f"Salary of the {self.company} Programmer {self.name} is {self.salary} and the product is {self.product}")    

sahil = Programmer("Sahil", 10000,"Teams")
ayush = Programmer("Ayush", 20000, "Skype")

sahil.getInfo()
ayush.getInfo()