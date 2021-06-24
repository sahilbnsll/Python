words = ['donkey','kaddu','mote','gadhe']

with open('problem04.txt') as f:
    content = f.read()
    
for word in words:
    content = content.replace(word, "#####")
    with open('problem04.txt', 'w') as f:
        f.write(content)