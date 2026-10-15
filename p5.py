bill = float(input("Enter the bill amount: "))
tip_percent = float(input("Enter the tip percentage: "))
people = int(input("How many people are splitting the bill? "))

tip = bill * tip_percent / 100
total = bill + tip
per_person = total / people

print("Tip:", tip)
print("Total: ", total)
print("Each person pays: ", per_person)