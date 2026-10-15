num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
sum=num1+num2
difference=num1-num2
product=num1*num2
print("Sum:", sum)
print("Difference:", difference)
print("Product:", product)
#program 2
name = input("Enter your name: ")
print(name.upper())
print(len(name))
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
#Ask for an age and print “child”, “teen”, “adult”, or “senior”.
age=int(input("Enter your age: "))
if age<13:
    print("Child")
elif age<20:
    print("Teen")
elif age<65:
    print("Adult")
else:
    print("Senior")
#progrmam 6
bill = float(input("Enter the bill amount: "))
tip_percent = float(input("Enter the tip percentage: "))
people = int(input("How many people are splitting the bill? "))

tip = bill * tip_percent / 100
total = bill + tip
per_person = total / people

print("Tip:", tip)
print("Total: ", total)
print("Each person pays: ", per_person)