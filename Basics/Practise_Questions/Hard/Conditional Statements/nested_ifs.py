'''Rewrite this using nested ifs without and/or

age = 25
income = 40000
has_degree = True

if age >= 21 and income >= 30000 and has_degree:
    print("Job offer extended")'''

def func(age,income,has_degree):
    if age >=21:
        if income >= 30000:
            if has_degree:
                print("Job offer Extednded")
func(21,30000,True)