# Property Decorator


class Employee:
    company = "Idea"
    salary = 10000
    salarybonus  = 5009

    @property
    def totalSalary(self):
        return self.salary + self.salarybonus

    @totalSalary.setter
    def totalSalary(self, value):
        self.salarybonus = value - self.salary    

e = Employee()
print(e.totalSalary)
e.totalSalary  = 3769
print(e.salary)
print(e.salarybonus)
        