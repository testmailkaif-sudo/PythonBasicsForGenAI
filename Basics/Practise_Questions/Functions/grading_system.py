
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

def report_card(name,*marks):
    avg = sum(marks)/len(marks)
    return grading_sys(avg)

report_card("Kaif",90,70,80)