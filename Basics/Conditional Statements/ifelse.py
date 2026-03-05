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