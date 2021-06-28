# Class Method

class Employee:
    company = "ClassMate"
    product = "Pen"
    price = 30
    location = "Dehradun"

    # def changePrice(self, rate):
    #     self.__class__.price = rate
    #     Above  Method does same as Below

    @classmethod
    def changePrice(cls ,rate):
       cls.price = rate

e = Employee()
print(e.price)
e.changePrice(40)
print(e.price)
print(Employee.price)