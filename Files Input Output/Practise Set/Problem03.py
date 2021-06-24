# Problem 3. Replace Bad words with sensors.

with open('problem03.txt') as f:
    content = f.read()

content = content.replace("bastard", "#####")
with open('problem03.txt', 'w') as f:
    f.write(content)
