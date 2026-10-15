# .py → Python → python project1.py
print("=== Study Hours Calculator ===")

hours = float(input("Hours studied per day: "))
days = int(input("Number of study days: "))
total_study_hours = hours * days
# TODO 1: Calculate total study hours.
total = total_study_hours

print("Your planned study hours:", total)

# TODO 2: If total is at least 100, print
if total>= 100:
    print("Great commitment!")
else:
    print("Keep building your habit.")
# "Great commitment!" Otherwise print
# "Keep building your habit."

