# Coping Content of problem01.txt in problem06.txt.

with open('problem01.txt') as f:
    content = f.read()

with open('problem06.txt', 'w') as f:
    f.write(content)    
