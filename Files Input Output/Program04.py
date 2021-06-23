# With Statement 

with open('sample04.txt', 'r') as f:
    # by using with statement, you don't need to close the file as f.close() as it automatically done
    a = f.read()
    print(a)

with open('sample04.txt', 'w') as f:
    a = f.write("With Statement Writing") #this line should be overwrite in your sample file
    