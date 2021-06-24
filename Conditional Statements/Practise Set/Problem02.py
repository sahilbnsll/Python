# problem 2. student pass or fail

sub1 = int(input("Enter marks in subject 1:"))
sub2 = int(input("Enter marks in subject 2:"))
sub3 = int(input("Enter marks in subject 3:"))
total=(sub1+sub2+sub3)/3
if(sub1<33 or sub2<33 or sub3<33):
    print("You are Fail because you have less than 33% in one of the subjects")
elif(total<40):
    print("You are Fail because you don't pass the criteria of 40%")
else:
    print("Congratulations!, You Passed the exam")    

