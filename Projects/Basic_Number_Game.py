# Basic Number Game

while(True):
    print("Press 'q' to quit.")
    num =input("Enter a Number: ")
    if num == 'q':
        break
    try:
        print("Trying...")
        num = int(num)
        if num >= 6:
            print("Your Entered Number is Greater than or equal to 6\n")

    except Exception as e:
        print(f"Your Input Resulted in an Error:{e}")        

print("Thanks For Playing.")