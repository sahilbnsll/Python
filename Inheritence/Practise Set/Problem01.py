# Problem 1. Creating a Class 2d vector and use it to create another class representing 3-d vector.

class C2dVector:
    def __init__(self, i, j):
        self.icap = i
        self.jcap = j

    def __str__(self):
        return f"{self.icap}i + {self.jcap}j"
            

class C3dVector(C2dVector):
    def __init__(self, i, j, k):
        super().__init__(i,j)
        self.kcap = k

    def __str__(self):
        return f"{self.icap}i + {self.jcap}j + {self.kcap}k"

v2d = C2dVector(1,7)
v3d = C3dVector(2,6,8)
print (v2d)               
print (v3d)               