# Finding Maximum of Three numbers

def maximum(num1,num2,num3):
    if(num1>num2):
        if(num1>num3):
            return num1
        else:
            return num3    
    else:
       if(num2>num3):
            return num2
       else:
            return num3   
a=int(input("Enter number 1: "))
b=int(input("Enter number 2: "))
c=int(input("Enter number 3: "))
m = maximum(a,b,c)        
print("the max. of three numbers  is " +str(m))