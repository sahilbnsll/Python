# # Dictionary

myDict = {
"Upes" : "University with a Purpose",
"Sahil" : "A Student and a Programmer",
"Marks" : [3,6,9],
"anotherDict": {'Sahil' : 'Gamer'},
1: 2
}
# print(myDict['Upes'])
# print(myDict['Sahil'])
# print(myDict['Marks'])
# print(myDict['anotherDict']['Sahil'])


# # Dictionary Methods

# print(myDict.keys()) # Prints the keys in a dictionary

# print(list(myDict.keys())) # Prints the list of keys in a dictionary

# print(myDict.values()) # Prints the keys values in a dictionary
# print(myDict.items()) # returns the list of (key : value) tuples

# print(myDict)
# updateDict = {
#     "Dhruv" : "Friend" ,
#     "Kshitij" : "Friend"
# }
# myDict.update(updateDict) # Update the dictionary by adding key-value pairs from updateDict
# print(myDict)

# print(myDict.get("Sahil2")) # Returns none as Sahil2 is not present in the dictionary
print(myDict.get("Sahil")) # Prints value associated with Sahil
# print(myDict["Sahil2"]) # Throws error as Sahil2 is not present in the dictionary