name = "Alice"
age = 25

# Old way ❌
print("My name is " + name + " and I am " + str(age))

# f-string ✅
print(f"My name is {name} and I am {age}")

# Can even do expressions inside {}
print(f"Next year I will be {age + 1}")
print(f"2 + 2 = {2 + 2}")