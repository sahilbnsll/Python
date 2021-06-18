# Indroduction to sets in Python
a = {1,5,4,8,9}
print(a)
print(type(a))

# Methods in Sets
b = {} # not an empty set
print(type(b)) # It will return a class dictionary

c = set() # Empty set
print(type(c)) # it will return a class set

# Adding values to an empty set
c.add(5)  
c.add(5)
c.add(6)
c.add((1,3,4)) # we can add tuple to sets but we can't add list or dictionary to the set 
c.add(6)
c.add(6)
print(c) # set is a collecion of non repeatable values

print(len(c)) # Prints lenght of this set

c.remove(5) # deletes element in a set
print(c)

print(a.pop())    #removes an element from the set and print the element that was removed
a.clear() #make set empty
print(a)

# problem - print 8 unique numbers entered by user
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))
num4 = int(input("Enter number 4: "))
num5 = int(input("Enter number 5: "))
num6 = int(input("Enter number 6: "))
num7 = int(input("Enter number 7: "))
num8 = int(input("Enter number 8: "))

s={num1,num2,num3,num4,num5,num6,num7,num8}
print(s)

# problem - can we have a set with 18(int) and "18"(string) as a values in it?
t= {18,"18",18.18}
print(t)