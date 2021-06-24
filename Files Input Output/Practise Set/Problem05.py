# Problem 5. Checking If Desired Word is present in Text file or not.

content = True
i=1
with open('problem05.txt') as f:
    while content:
        content = f.readline()
        if 'python' in content.lower():
                print(content)
                print(f"Yes, 'python' is present on line number {i}")
        i+=1 