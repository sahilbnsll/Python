# writing in Text file using Python

f = open('sample03.txt', 'a')

# f.write("I am Writing this to the file sample03.txt") # Creates sample03.txt and write this line to file.

f.write("\nI am appending") #add I am appending to the end of a file every you run the program

f.close()