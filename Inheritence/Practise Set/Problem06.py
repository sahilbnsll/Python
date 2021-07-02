# Problem 6. Write __str__ method to print a 3-d vector

class Vector:
    def __init__(self, vec):
        self.vec = vec

    def __str__(self):
       return f"{self.vec[0]}i + {self.vec[1]}j + {self.vec[2]}k"

v1 = Vector([3,6,7])
v2 = Vector([3,5,1])
print(v1)        