# Problem 2. Create a class pets from animal and further create a class dog and add a method bark to the class dog.

class Animals:
    animalType = "Mammal"

class Pets(Animals):
    color ="white"

class Dog(Pets):
    @staticmethod
    def bark():
        print("BOW BOW!")


d = Dog()
d.bark()