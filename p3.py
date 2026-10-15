#program 3 Ask for a temperature in Celsius and convert it to Fahrenheit (F = C * 9/5 + 32).
temperature_cel=float(input("Enter temperature in Celsius:  ")) 
fahrenheit = temperature_cel * 9/5 + 32
print("Temperature in Fahrenheit:", fahrenheit)
#Ask for a number and say whether it is even or odd (hint: %).
number=int(input("Enter a number: "))
if number%2==0:
    print("The number is even.")
else:
    print("The number is odd.")