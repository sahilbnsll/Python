# # Dictionary

from typing import ValuesView


myDict = {
"Upes" : "University with a Purpose",
"Sahil" : "A Student and a Programmer",
"Marks" : [3,6,9],
"anotherDict": {'Sahil' : 'Gamer'},
1: 2
}
print(myDict['Upes'])
print(myDict['Sahil'])
print(myDict['Marks'])
print(myDict['anotherDict']['Sahil'])


# # Dictionary Methods

print(list(myDict.keys())) # Prints the list of keys in a dictionary

print(myDict.values()) # Prints the keys values in a dictionary
print(myDict.items()) # returns the list of (key : value) tuples

print(myDict)
updateDict = {
    "Dhruv" : "Friend" ,
    "Kshitij" : "Friend"
}
myDict.update(updateDict) # Update the dictionary by adding key-value pairs from updateDict
print(myDict)

print(myDict.get("Sahil2")) # Returns none as Sahil2 is not present in the dictionary
print(myDict.get("Sahil")) # Prints value associated with Sahil
# print(myDict["Sahil2"]) # Throws error as Sahil2 is not present in the dictionary


# Problem - Hindi Dictionary
hindiDict = {
    "pankha" : "Fan",
    "gaadi" : "Car",
    "baksha" : "Box",
    "vastu" : "Item"
}
print("Your options are: ",hindiDict.keys())
a = input("Enter your hindi word\n")
# print("Meaning of this word is ",hindiDict[a])

# Below line will not throw error if the key is not present
print("Meaning of this word is: ",hindiDict.get(a))



# problem - allow 4 friends to enter their favourite language as Values
favLang={}
a= input("Enter your favourite language Sahil: ")
b= input("Enter your favourite language Dhruv: ")
c= input("Enter your favourite language Kshitij: ")
d= input("Enter your favourite language Parth: ")
favLang['Sahil'] = a
favLang['Dhruv'] = b
favLang['Kshitij'] = c
favLang['Parth'] = d
print(favLang)