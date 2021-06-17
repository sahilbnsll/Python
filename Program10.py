# Creating a Tuple using ()
t = (1,4,6,9,1,3,5,1,4,1)
print(t)

print(t[2]) # Printing the elements of tuple at inpex 2

t1=() # This is an empty tuple
print(t1)

#t[0] =34  --> Tuples values are immutable(cannot be changed) --> Throws a Error
t2=(1) # Wrong way to declare a tuple with single element
t2=(1,) # Correct way to declare a tuple with single element
print(t2)

#  Tuple Methods

print(t.count(1)) # Return number of occurence of values

print(t.index(9)) # Return first index of value