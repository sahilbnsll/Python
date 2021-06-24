# Problem 1. Program that reads a text file and check whether the file contain a specific word or not

f = open('problem01.txt')
p = f.read()
word =input("Enter a Word: ")
if(word in p.lower()):
    print(f"'{word}' is present in file")
else:
    print(f"'{word}' is not present in file")
