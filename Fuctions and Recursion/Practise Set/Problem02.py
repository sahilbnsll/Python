# Convert celsius into fahrenheit

def celsius(c):
    return (c * 9/5) +32

c= int(input("Enter the Degree in Celsius: "))
print("Converted Fahrenheit Degree is: "+ str(celsius(c)))    