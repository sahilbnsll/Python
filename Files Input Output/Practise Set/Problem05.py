content = True
i=1
with open('problem05.txt') as f:
    while content:
        content = f.readline()
        if 'python' in content.lower():
                print(content)
                print(f"Yes, 'python' is present on line number {i}")
        i+=1 
               
                