# Problem 1. - Hindi Dictionary

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
