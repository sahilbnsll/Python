# Problem 4. Adding a static method to greet the user in problem 2.

class Calculator:
    def __init__(self,num,name):
        self.names = name
        self.number = num

    def square(self):
            print(f"The Value of {self.number} square is: {self.number **2}")

    def cube(self):
            print(f"The Value of {self.number} cube is: {self.number **3}")

    def squareRoot(self):
          print(f"The Value of {self.number} Square Root is: {self.number **0.5}")

    @staticmethod
    def greet():
        print(f"Good Morning, {a.names} Sir")      

a = Calculator(int(input()),"Sahil")
a.greet()
a.square()
a.squareRoot()
a.cube()