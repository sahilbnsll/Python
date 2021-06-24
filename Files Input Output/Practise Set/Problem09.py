# Rename the Text File 
import os

oldFile = 'problem09.txt'
newFile = 'problem09(renamed).txt'

with open(oldFile) as f:
    content = f.read()

with open(newFile, 'w') as f:
    f.write(content)

os.remove(oldFile)    

