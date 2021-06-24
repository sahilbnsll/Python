class Employee:
    company= "Google Inc."
    salary = 30000
    def getAdress(self):
        print("Address is Bari")

sahil = Employee()     
ayush = Employee()     

Employee.getAdress(sahil)
sahil.salary = 40000
print(sahil.company)
print(sahil.salary)

print(ayush.company)
print(ayush.salary)
