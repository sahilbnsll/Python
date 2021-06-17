# Creating the List using []
a = [24, 12 ,17]

# print the list using print() function
print(a)

# access element of list at different indexes
print(a[2])

# change the value of element in list
a[1] = 6
print(a)

# we can create a list with different item Types
c = [24, "Sahil", True, 6.9]
print(c)

# List Slicing
friends = ["Dhruv", "Kshitij", "Mansukh", "Abhay", "Ankush", 24]
print(friends[0:4])
print(friends[-4:])

# List Methods
l1 = [1,8,45,12,9,2,7]
l1.sort() #Sorts the list in ascending order
print(l1)

l1.reverse() #Sorts in list in reverse(Descesding order)
print(l1)

l1.append(69) # adds 69 at the end of the list
print(l1)

l1.insert(0, 34) #adds 34 at index 0
print(l1)

l1.pop(2) #Removes element at index 2
print(l1)


l1.remove(69) #Removes 69 from the list
print(l1)


# # Fruit list Program
f1 = input("Enter Fruit Number 1: ")
f2 = input("Enter Fruit Number 2: ")
f3 = input("Enter Fruit Number 3: ")
f4 = input("Enter Fruit Number 4: ")
f5 = input("Enter Fruit Number 5: ")
f6 = input("Enter Fruit Number 6: ")
f7 = input("Enter Fruit Number 7: ")
myFruitList = [f1,f2,f3,f4,f5,f6,f7]
print(myFruitList)

# Sorting marks of 6 Students
m1 = int(input("Enter marks of student number 1: "))
m2 = int(input("Enter marks of student number 2: "))
m3 = int(input("Enter marks of student number 3: "))
m4 = int(input("Enter marks of student number 4: "))
m5 = int(input("Enter marks of student number 5: "))
m6 = int(input("Enter marks of student number 6: "))

myList = [m1,m2,m3,m4,m5,m6]
myList.sort()
print(myList)

# adding elements of a list
list1 = [2,78,97,34,23]
print(sum(list1)) # Adding Elements using sum() Function