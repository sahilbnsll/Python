# Reading text file using Python

# use open function to read the content of a file
f = open('sample.txt', 'r') # here 'r' stands for read. In open() function, by default mode is 'r'
data = f.read()
print(data)
f.close # use close function to close the file.