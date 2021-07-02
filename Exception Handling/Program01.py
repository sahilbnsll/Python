# try-Except Statements

try:
    a = 10
    b = 0
    c= a/b

except Exception as e:
    print("Can't divide by zero")
    print(e)    