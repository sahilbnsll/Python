class Calculator:
    def __init__(self,num):
        self.number = num

    def square(self):
            print(f"The Value of {self.number} square is: {self.number **2}")

    def cube(self):
            print(f"The Value of {self.number} cube is: {self.number **3}")

    def squareRoot(self):
          print(f"The Value of {self.number} Square Root is: {self.number **0.5}")

a = Calculator(int(input()))
a.square()
a.squareRoot()
a.cube()