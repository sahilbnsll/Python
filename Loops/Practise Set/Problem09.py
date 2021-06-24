# Problem 9. Write a program to print the following star pattern: * * *
                                    #                             *   *             
                                             #                    * * * 

n=3
for i in range(n):
    print("x" * (2*n-2*i-3),end="")
    print(" " *(n-2*i),end="")
    print("x" * (n+2*i-4))


