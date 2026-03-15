"""A student passes if marks are 50 or above. Print "Pass" or "Fail"."""
def grading_system(marks):
    if marks >= 50: print("Pass")
    else : print("Fail")
grading_system(int(input("Enter the marks of the students : ")))