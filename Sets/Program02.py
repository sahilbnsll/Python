# Methods in Sets

a = {1,5,4,8,9} 

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