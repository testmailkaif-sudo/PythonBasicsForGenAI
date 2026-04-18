'''Build a student database:

add_student(db, name, age, subjects) → subjects is a list, name stored in title case
search_student(db, name) → case-insensitive search, print full details
students_by_subject(db, subject) → return list of students taking that subject
summary(db) → print total students, all unique subjects (use a set), oldest and youngest student'''
db ={}
def add_students(db, name, age, subjects):
    name=name.title()
    db[name]={
        'age':age,
        'subjects':list(subjects)
    }
    return db
def serch_students(db, name):
    name = name.title()
    if name in db:
        subjects = " , ".join(db[name]["subjects"])
        print("Name -",name, "Age - ", db[name]['age'],"Subjects - ",subjects)
    else:
        print("Not Found")
def students_by_subjects(db, subject):
    result = []
    for name, details in db.items():
        if subject in details['subjects']:
            result.append(name)
    return result

def summary(db):
    total_students = len(db)
    all_subjects = set()
    for details in db.values():
        for subject in details['subjects']:
            all_subjects.add(subject)
    max_age=0
    min_age = float('inf')
    oldest_name, youngest_name = None,None
    for name,details in db.items():
        age = details['age']
        if age > max_age:
            max_age = age
            oldest_name = name
        if age <min_age:
            min_age = age
            youngest_name = name
    print("Total Students are = ", total_students)
    print("All subjects are ",all_subjects)
    print("Youngest is ", youngest_name," his age is ", min_age)
    print("Oldest is ", oldest_name, " his age is ", max_age)
add_students(db, "kaif", 22, ["Math","physics","english"])
add_students(db, "mastan", 25, ["Math","science","Telugu"])
serch_students(db,"kaif")
students_by_subjects(db,'Math')
print(summary(db))