# a key value based data collection. like a real dictionary

student = {
    "name" : "Kaif",
    "age" : 23,
    "grade" : "A"
}

#accessing values in dictionary

print(student["name"])
print(student.get("age"))
print(student.get("result","N/A"))

#Modifying a dictionary

student["name"] = "Hussain" # edit
student["result"] = "Pass" #add parameter
print(student)
del student["result"]
print(student)
student.pop("age")
print(student)

#methods
print(student.keys())
print(student.values())
print(student.items())
print(len(student))
print("name" in student)


#Looping a dictionary
student = {
    "name" : "Kaif",
    "age" : 23,
    "grade" : "A",
    "result" : "Pass"
}

for key in student:
    print(key, student[key])
for key, values in student.items():
    print(key,values)


#Nested Dictionary's

Students={
    "Kaif": {"roll_number":"20H71A04E0","Grade":7.75},
    "Pushpa":{"roll_number":"20H71A04E1","Grade":7.80}
}