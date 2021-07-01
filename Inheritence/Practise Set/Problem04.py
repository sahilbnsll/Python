# Problem 4. Create a class Complex that represents complex numbers along with overloaded operators.

class Complex:
    def __init__(self,r,i):
        self.real = r
        self.imaginary = i
    
    def __add__(self,c):
        return Complex(self.real + c.real, self.imaginary+ c.imaginary)
    
    def __mul__(self,c):
        return Complex(self.real * c.real - self.imaginary * c.imaginary, self.imaginary * c.real + self.real * c.imaginary)

    def __str__(self):
        return f"{self.real} + {self.imaginary}i"    


c1 = Complex(1,2)
c2 = Complex(2,1)
print(c1 + c2)
print(c1 * c2)