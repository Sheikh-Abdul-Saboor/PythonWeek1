#Python Week 2 Codes 
#Section A while loops
#Program 1 
#Q1. Numbers 1 to 10
#Code: 
i = 1
while i <= 10:
    print(i)
    i += 1
    #Program 2
#Q2. Even numbers 2 to 20
#Code: 
i = 2
while i <= 20:
    print(i, end=" ")
    i += 2
print()
 #Program 3
#Q3. Count down from a user input number to 1
#Code: 
n = int(input("Enter a number: "))
while n >= 1:
    print(n)
    n -= 1
print("Go!")
#Program 4
#Q4. Password loop
#Code: 
password = input("Enter password: ")
while password != "python":
    print("Wrong password, try again.")
    password = input("Enter password: ")
print("Access granted")
#program 5
#Section B: for loops and accumulators
#Q5. Multiplication table
n = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")
#program 6
#Q6. Sum of 1 to n
#Code:
n = int(input("Enter n: "))
total = 0
for i in range(1, n + 1):
    total += i
print("Sum:", total)
#program 7
#Q7. Sum of even numbers up to n
n = int(input("Enter n: "))
total = 0
for i in range(2, n + 1, 2):
    total += i
print("Sum of evens:", total)
#program 8
#Q8. Factorial
n = int(input("Enter a number: "))
result = 1
for i in range(1, n + 1):
    result *= i
print(f"{n}! = {result}")
#program 9
#Q9. Count vowels
word = input("Enter a word: ").lower()
vowels = 0
for ch in word:
    if ch in "aeiou":
        vowels += 1
print("Vowels:", vowels)
#Program 10
#Q10. Print each character with its index
word = input("Enter a word: ")
for i in range(len(word)):
    print(i, word[i])
    #Program 11
    #Q11. Average of numbers
    count = int(input("How many numbers? "))
total = 0
for i in range(count):
    total += float(input(f"Enter number {i + 1}: "))
print("Average:", total / count)
#Section C: break, continue, validation
#Program 12
#Q12. Keep asking until the number is positive
while True:
    number = float(input("Enter a positive number: "))
    if number > 0:
        break
    print("That is not positive, try again.")
print("You entered", number)
#Q13. 1 to 20, skipping multiples of 3
for i in range(1, 21):
    if i % 3 == 0:
        continue
    print(i, end=" ")
print()
#Q14. First number from 1 to 100 divisible by both 7 and 11
for i in range(1, 101):
    if i % 7 == 0 and i % 11 == 0:
        print("First number divisible by both 7 and 11:", i)
        break
    #Section D: nested loops and patterns

#Q15. Star triangle
n = int(input("Enter number of rows: "))
for row in range(1, n + 1):
    print("*" * row)
    #Q16. Number triangle
    #code:
    n = int(input("Enter number of rows: "))
for row in range(1, n + 1):
    for num in range(1, row + 1):
        print(num, end="")
    print()
    #Q17. 5 x 5 multiplication grid
    #code:
for row in range(1, 6):
    for col in range(1, 6):
        print(row * col, end="\t")
    print()
    #Section E: Challenges

#Q18. Prime checker
#Code
n = int(input("Enter a number: "))

if n < 2:
    is_prime = False
else:
    is_prime = True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            is_prime = False
            break

if is_prime:
    print(n, "is prime")
else:
    print(n, "is not prime")
    #Q19. Fibonacci numbers
    #Code
    n = int(input("How many terms? "))
a, b = 0, 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
print()
#Q20. Digit sum
#Code:
number = int(input("Enter a number: "))
total = 0
while number > 0:
    total += number % 10    # last digit
    number //= 10           # remove last digit
print("Digit sum:", total)