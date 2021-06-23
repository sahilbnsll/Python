# Reading text file using Python

# use open function to read the content of a file
f = open('sample01.txt', 'r') # here 'r' stands for read. In open() function, by default mode is 'r'
data = f.read() 
# we cannot run read() function more than 1 time in program

# data = f.read(8) # read first 8 characters from a file.

print(data)
f.close # use close function to close the file.