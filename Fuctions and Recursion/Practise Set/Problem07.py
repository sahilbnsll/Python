# Function to remove a word from String and Strip it at same time

# text= "      Sahil is a Good Boy         "
# print(text)  # Prints Exact String 
# print(text.strip())  # Removes Extra spaces in string

def remove_strip(string, word):
    newStr = string.replace(word, "")
    return newStr.strip()

paragraph = "Python is a general-purpose programming language, so it can be used for many things. Python is used for web development, AI, machine learning, operating systems, mobile application development, and video games"

p = remove_strip(paragraph, "Python")
print(p)