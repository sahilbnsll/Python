class Employee:
    company= "Google Inc."
    def getSalary(self, signature):
        print(f"Salary for employee working in {self.company} is {self.salary}\n{signature}")
        
    @staticmethod
    def greet():
        print("Good Morning, Sir")


sahil= Employee()
sahil.salary = 1000000
sahil.greet()
sahil.getSalary("Thanks")