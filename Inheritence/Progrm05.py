# Property Decorator


class Employee:
    company = "Idea"
    salary = 10000
    salarybonus  = 5009

    @property
    def totalSalary(self):
        return self.salary + self.salarybonus

e = Employee()
print(e.totalSalary)
        