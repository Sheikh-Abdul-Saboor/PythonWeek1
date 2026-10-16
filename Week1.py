#Python Week 1 Codes 

#Program 1 

#Code: 

num1=int(input("Enter first number: ")) 

num2=int(input("Enter second number: ")) 

sum=num1+num2 

difference=num1-num2 

product=num1*num2 

print("Sum:", sum) 

print("Difference:", difference) 

print("Product:", product) 

#Output: 

 

#Program 2 

#Code 

name = input("Enter your name: ") 

print(name.upper()) 

print(len(name)) 

#Output: 
 

#Program 3 

#Ask for a temperature in Celsius and convert it to Fahrenheit (F = C * 9/5 + 32). 

temperature_cel=float(input("Enter temperature in Celsius:  "))  

fahrenheit = temperature_cel * 9/5 + 32 

print("Temperature in Fahrenheit:", fahrenheit) 

#Output: 

 

#Program 4 

#Ask for a number and say whether it is even or odd (hint: %). 

number=int(input("Enter a number: ")) 

if number%2==0: 

    print("The number is even.") 

else: 

    print("The number is odd.") 

#Output: 

 

#Program 5: 

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

#Output: 

 

#Program 6 

#Code: 

bill = float(input("Enter the bill amount: ")) 

tip_percent = float(input("Enter the tip percentage: ")) 

people = int(input("How many people are splitting the bill? ")) 

  

tip = bill * tip_percent / 100 

total = bill + tip 

per_person = total / people 

  

print("Tip:", tip) 

print("Total: ", total) 

print("Each person pays: ", per_person) 

#Output: 

 

#Basic Project Code: 

#.py → Python → python project1.py 

print("=== Study Hours Calculator ===") 

hours = float(input("Hours studied per day: ")) 

days = int(input("Number of study days: "))  

total_study_hours = hours * days 

#TODO_1: Calculate total study hours. 

total = total_study_hours 

print("Your planned study hours:", total) 

#TODO_2: If total is at least 100, print 

if total>= 100:  
 print("Great commitment!") 
else:  
 print("Keep building your habit.") 

#"Great commitment!" Otherwise print 

#"Keep building your habit." 

#Output: 

 

#Program7: 

#Ask for a name. Print a greeting that includes how many letters the name has. 

#Code: 

name = input("Enter your name: ") 
 
print(f"Hello, {name}! Your name has {len(name.replace(' ', ''))} letters.") 
#How it works: 
#- name.replace(' ', '') removes spaces from the name. 
#- len(...) counts the remaining characters. 
#- The space between Ali and Khan is not counted. 

#Output: 

 

 

#Program 8: 

#First and last character 

#Code: 

word = input("Enter a word: ") 
print("First:", word[0]) 
print("Last:", word[-1]) 
# word[-1] — Last character 
# Python also allows negative indexing, which counts from the end of a string. 

#Output: 

 

#Program 9: 

#Reverse a word 

#Code: 

word = input("Enter a word: ") 

print(word[::-1]) 

# [::-1] means “take everything, stepping backwards by 1.” 

#Output: 

 

#Program 10: 

#Lowercase and spaces 

#Code: 

sentence = input("Enter a sentence: ") 

print(sentence.lower()) 

print("Spaces:", sentence.count(" ")) 

#Output: 

 

#Program 11: 

#Replace a word 

#Code: 
sentence = input("Enter a sentence: ") 
print(sentence.replace("BAD", "GOOD")) 
#Output: 

 

#Program 12: 

#Name format 

#Code: 

first = input("First name: ") 

last = input("Last name: ") 

print(f"{last}, {first}") 

#Output: 

 

#Program 13: 

#Positive, negative, or zero 

#Code: 

number = float(input("Enter a number: ")) 
 
if number > 0: 
    print("positive") 
elif number < 0: 
    print("negative") 
else: 
    print("zero") 

#Output: 

 

#Program 14: 

#Largest of three 

#Code: 

a = float(input("Enter first number: ")) 

b = float(input("Enter second number: ")) 

c = float(input("Enter third number: ")) 

if a >= b and a >= c: 

    largest = a 

elif b >= a and b >= c: 

    largest = b 

else: 

    largest = c  

print("Largest:", largest) 

#Output: 

 

#Program 15: 

#Leap year 

year = int(input("Enter a year: ")) 

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0): 

    print(f"{year} is a leap year") 

else: 

    print(f"{year} is not a leap year") 

#Output: 

 

#Program 16: 

#Grade calculator 

score = float(input("Enter your score: ")) 

if score >= 90: 

    grade = "A" 

elif score >= 80: 

    grade = "B" 

elif score >= 70: 

    grade = "C" 

elif score >= 60: 

    grade = "D" 

else: 

    grade = "F" 

print("Grade:", grade) 

#Output: 

 

#Program 17: 

#Login check 

correct_username = "kiba" 

correct_password = "python123" 

 

username = input("Username: ") 

password = input("Password: ") 

 

if username == correct_username and password == correct_password: 

    print("Access granted") 

else: 

    print("Access denied") 

#Output: 

 

#Program 18: 

#Divisible by 3 and 5 

number = int(input("Enter a number: ")) 

if number % 3 == 0 and number % 5 == 0: 

    print("Divisible by both 3 and 5") 

elif number % 3 == 0: 

    print("Divisible by 3 only") 

elif number % 5 == 0: 

    print("Divisible by 5 only") 

else: 

    print("Divisible by neither") 

#Output: 
 

#Program 19 

#Valid triangle 

a = float(input("Side 1: ")) 

b = float(input("Side 2: ")) 

c = float(input("Side 3: ")) 

  

if a + b > c and a + c > b and b + c > a: 

    print("These sides can form a triangle") 

else: 

    print("These sides cannot form a triangle") 

#Output: 

 

#Program 20 

#BMI Calculator 

#Code: 

weight = float(input("Weight in kg: ")) 
height = float(input("Height in meters: ")) 

bmi = weight / height ** 2 

if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal"
elif bmi < 30:
    category = "Overweight"
else:
    category = "Obese"

print(f"BMI: {bmi:.2f} ({category})") 

#1. What does f mean? 

#The f before a string means formatted string literal (f-string). It allows you to put variables inside a string using {}. 

#Output: 

 

#Program 21 

#Simple interest calculator 

#Code: 

principal = float(input("Enter principal amount: ")) 

rate = float(input("Enter rate of interest (%): "))  

time = float(input("Enter time (years): ")) 

interest = principal * rate * time / 100 

total = principal + interest 

print(f"Interest: {interest:.2f}") 

print(f"Total amount: {total:.2f}") 

#Output: 

 

#Program 22: 

#Electricity bill  

#Code: 

units = int(input("Enter units consumed: ")) 

if units <= 100: 
    bill = units * 10
else: 
    bill = 100 * 10 + (units - 100) * 15 

print(f"Electricity bill: {bill}") 


 

#Program 23: 

#Ticket Pricing 

#Code: 

age = int(input("Enter your age: ")) 

weekend = input("Is it a weekend? (yes/no): ").lower() 

  

if age < 12: 

    price = 5 

elif age < 60: 

    price = 10 

else: 

    price = 6 

  

if weekend == "yes": 

    price = price + 2 

  

print(f"Ticket price: {price}") 

#Output: 

 
