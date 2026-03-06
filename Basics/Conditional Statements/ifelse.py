"""Indentation is mandatory while using the conditional statements"""
#If
age = 20
if age >= 18:
    print("You are an adult")   # this runs only if the condition is True

# If-Else
age = 15

if age >= 18:
    print("You are an adult") # this runs only if the condition is True
else:
    print("You are a minor")    # this runs when condition is False

#If-Elif-else

marks = 72

if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")    # this runs
else:
    print("Grade: F")


#NestedIf
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed")   # this runs
    else:
        print("No ID, entry denied")
else:
    print("Too young")

#Shorthand if or Ternary Operator
age = 20
status = "Adult" if age >= 18 else "Minor"
print(status)   # Adult

# If with logical operators
age = 25
income = 50000

if age >= 18 and income >= 30000:
    print("Loan approved")   # this runs

if age < 18 or income < 10000:
    print("Loan denied")     # doesn't run

#in and not in with If statement
fruits = ["apple", "banana", "mango"]

if "apple" in fruits:
    print("Apple is available")     # this runs

if "grape" not in fruits:
    print("Grape is not available") # this runs


