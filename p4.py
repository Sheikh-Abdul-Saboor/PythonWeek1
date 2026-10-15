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