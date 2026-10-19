#Week 3 word file
#Task: Make the list ["apple", "banana", "cherry"]. Print the first item, the last item, and the length. Add "mango", remove "banana", then print the list. 

#Test it: Output: apple, cherry, 3, then the new list 

fruits = ["apple", "banana", "cherry"] 

print(fruits[0]) 

print(fruits[-1]) 

print(len(fruits)) 

fruits.append("mango") 

fruits.remove("banana") 

print(fruits) 
#Question 2: Sum, largest, smallest, average 

#Task: For the list [4, 9, 2, 7, 1], print the sum, the largest, the smallest, and the average. 

#Test it: Sum 23, largest 9, smallest 1, average 4.6 
numbers = [4, 9, 2, 7, 1] 

print("Sum:", sum(numbers)) 

print("Largest:", max(numbers)) 

print("Smallest:", min(numbers)) 

print("Average:", sum(numbers) / len(numbers)) 
#Question 3: Squares list 

#Task: Build a new list with the square of each number from 1 to 10. 

#Test it: [1, 4, 9, ... 100] 
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 

squares = [] 

for n in numbers: 

    squares.append(n * n) 

print(squares) 
#Question 4: Keep only the even numbers 

#Task: From [5, 12, 7, 20, 3, 18], make a new list with only the even numbers. 

#Test it: [12, 20, 18] 

numbers = [5, 12, 7, 20, 3, 18] 

evens = [] 

for n in numbers: 

    if n % 2 == 0: 

        evens.append(n) 

print("Evens:", evens) 
#Question 5: Sort three names 

#Task: Ask for 3 names, sort them, and print the sorted list and the first name. 

#Test it: Sara, Ali, Zain gives Ali first 
names = [] 

for i in range(3): 

    names.append(input(f"Enter name {i + 1}: ")) 

names.sort() 

print(names) 

print("First alphabetically:", names[0]) 

#Question 6: Reverse a list 

#Task: Reverse [1, 2, 3, 4, 5] in two different ways. 

#Test it: [5, 4, 3, 2, 1] 

#Solution 

numbers = [1, 2, 3, 4, 5] 

reversed_list = [] 

for n in numbers: 

    reversed_list.insert(0, n) 

print(reversed_list) 

print(numbers[::-1]) 

#Question 7: Count one value 

#Task: Ask for a number and count how many times it appears in [3, 8, 3, 1, 8, 8]. 

#Test it: 8 appears 3 times 

#Solution 

numbers = [3, 8, 3, 1, 8, 8] 

target = int(input("Count which number? ")) 

count = 0 

for n in numbers: 

    if n == target: 

        count += 1 

print(f"{target} appears {count} times") 

#Question 8: Remove duplicates 

#Task: Remove the duplicates from [3, 8, 3, 1, 8, 8], keeping the original order. 

#Test it: [3, 8, 1] 

#Solution 

numbers = [3, 8, 3, 1, 8, 8] 

unique = [] 

for n in numbers: 

    if n not in unique: 

        unique.append(n) 

print(unique) 
#Question 9: Passed count and highest mark 

#Task: For [72, 85, 90, 65, 58], count how many marks are 60 or more, and find the highest mark and its position. 

#Test it: Passed 4 of 5, highest 90 at position 2 

#Solution 

marks = [72, 85, 90, 65, 58] 

passed = 0 

for m in marks: 

    if m >= 60: 

        passed += 1 

print("Passed:", passed, "of", len(marks)) 

print("Highest:", max(marks), "at position", marks.index(max(marks))) 

#Question 10: Student dictionary 

#Task: Make a dictionary with name, age, and city. Print the name, change the age to 21, add a grade of "A", then safely look up a "phone" key that does not exist. 

#Test it: Last line prints Not found 

#Solution 

student = {"name": "Ali", "age": 20, "city": "Lahore"} 

print(student["name"]) 

student["age"] = 21 

student["grade"] = "A" 

print(student) 

print(student.get("phone", "Not found")) 

#Question 11: Loop over a dictionary 

#Task: Loop over the student dictionary and print each key and value, in two different ways. 

#Test it: name -> Ali ... then name: Ali ... 

#Solution 

student = {"name": "Ali", "age": 20, "city": "Lahore"} 

for key in student: 

    print(key, "->", student[key]) 

print("---") 

for key, value in student.items(): 

    print(f"{key}: {value}") 

 #   Question 12: Letter counter 

#Task: Ask for a sentence and count how many times each letter appears, ignoring spaces. 

#Test it: hello world gives l 3, o 2 

#Solution 

text = input("Enter a sentence: ").lower() 

counts = {} 

for ch in text: 

    if ch != " ": 

        counts[ch] = counts.get(ch, 0) + 1 

for ch in counts: 

    print(ch, counts[ch]) 

 #   Question 13: Word counter 

#Task: Ask for a sentence and count how often each word appears. 

#Test it: the cat and the dog and the bird gives the: 3, and: 2 

#Solution 

sentence = input("Enter a sentence: ").lower() 

words = sentence.split() 

counts = {} 

for w in words: 

    counts[w] = counts.get(w, 0) + 1 

print(counts) 


#Question 14: Shop total 

#Task: Prices: apple 3, bread 2, milk 5. Keep asking for an item until the user types done, adding up the prices. Say if an item is not sold. Print the total. 

#Test it: apple, milk, pizza, bread, done gives total 10 

#Solution 

prices = {"apple": 3, "bread": 2, "milk": 5} 

total = 0 

while True: 

    item = input("Item (or done): ").lower() 

    if item == "done": 

        break 

    if item in prices: 

        total += prices[item] 

    else: 

        print("We do not sell that.") 

print("Total:", total) 

#Section C: Combining them 

#Questions 15 to 18. Lists and dictionaries together. 

#Question 15: List of dictionaries 

#Task: Students: Ali 72, Sara 91, Zain 58, stored as a list of dictionaries. Print the top student and the class average. 

#Test it: Top student Sara 91, average 73.7 

#Solution 

students = [ 

    {"name": "Ali", "marks": 72}, 

    {"name": "Sara", "marks": 91}, 

    {"name": "Zain", "marks": 58}, 

] 

best = students[0] 

for s in students: 

    if s["marks"] > best["marks"]: 

        best = s 

print("Top student:", best["name"], best["marks"]) 

total = 0 

for s in students: 

    total += s["marks"] 

print("Class average:", round(total / len(students), 1)) 

#Question 16: To-do list menu 

#Task: Show a menu to add a task, show tasks, remove a task by number, or quit. Repeat until the user quits. 

#Test it: Add Study and Gym, remove 1, show gives 1 Gym 

#Solution 

todo = [] 

while True: 

    print("1. Add  2. Show  3. Remove  4. Quit") 

    choice = input("Choose: ") 

    if choice == "1": 

        todo.append(input("Task: ")) 

    elif choice == "2": 

        for i in range(len(todo)): 

            print(i + 1, todo[i]) 

    elif choice == "3": 

        num = int(input("Number to remove: ")) 

        if 1 <= num <= len(todo): 

            todo.pop(num - 1) 

        else: 

            print("Invalid number") 

    elif choice == "4": 

        break 

    else: 

        print("Invalid choice") 

print("Bye") 

#Question 17: Grid (list of lists) 

#Task: Print the grid [[1,2,3],[4,5,6],[7,8,9]] row by row, then the sum of all the values. 

#Test it: Sum 45 

#Solution 

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] 

for row in matrix: 

    print(row) 

total = 0 

for row in matrix: 

    for value in row: 

        total += value 

print("Sum:", total) 

#Question 18: Common items 

#Task: Find the numbers that appear in both [1,2,3,4,5] and [4,5,6,7]. 

#Test it: Common: [4, 5] 

#Solution 

a = [1, 2, 3, 4, 5] 

b = [4, 5, 6, 7] 

common = [] 

for n in a: 

    if n in b: 

        common.append(n) 

print("Common:", common) 