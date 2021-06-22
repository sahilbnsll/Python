# Multiplication Table using function
def mutli_table(n):
    for i in range(1,11):
        print(n,'x',i,'=',n*i)

n=int(input("Enter a Number: "))
mutli_table(n)    