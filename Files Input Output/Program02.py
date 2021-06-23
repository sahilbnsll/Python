# Readline Function in Python

# readline() function reads one full line at a time from a file

f = open('sample02.txt')
# reads first line
data = f.readline()
print(data)

# reads second line
data = f.readline()
print(data)

# reads third line
data = f.readline()
print(data)

# reads fourth line
data = f.readline()
print(data)

# reads fifth line and so on.....
data = f.readline()
print(data)

f.close()