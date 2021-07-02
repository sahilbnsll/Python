# Problem 5. Creating a class Vector that represents n dimensions vector. overload + and * operatorswhich calculates sum and dot product.

class Vector:
    def __init__(self,vec):
        self.vec = vec

    def __str__(self):
        str1= ""
        index = 0
        for i in self.vec:
            str1 += f"{i}a{index} +"
            index += 1
        return str1[:-1]    

    def __add__(self,vec2):
        newList = []
        for i in range(len(self.vec)):
            newList.append(self.vec[i] + vec2.vec[i])
        return Vector(newList)    
   
    def __mul__(self,vec2):
        sum = 0
        for i in range(len(self.vec)):
            sum += self.vec[i] + vec2.vec[i]
        return sum    

v1 = Vector([2,3,1])
v2 = Vector([4,6,1])       
print(v1+v2)
print(v1*v2)