'''Build a grading system:

90–100 → "A"
75–89 → "B"
60–74 → "C"
45–59 → "D"
Below 45 → "F"'''


def grading_system(marks):
    if marks in range(90,101):
        print("A")
    elif marks in range(75,90):
        print("B")
    elif marks in range(60,75):
        print("C")
    elif marks in range(45,60):
        print("D")
    elif marks < 45:
        print("Fail")
grading_system(int(input("Enter the marks : ")))



'''Another Model of grading syatem is Below'''

def grading_sys(marks):
    if 90<= marks <=100:
        print("A")
    elif 75 <= marks <= 89:
        print("B")
    elif 60 <= marks <= 74:
        print("C")
    elif 45 <= marks <= 59:
        print("D")
    elif marks <45:
        print("Fail")
    else:
        print("Invalid Input")
grading_sys(int(input("Enter the number :")))