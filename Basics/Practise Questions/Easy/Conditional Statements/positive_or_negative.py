""" Write a program that checks if a number is positive, negative, or zero and prints the result"""

def positive_or_negative(num):
    if num > 0 :print("Number is positive :",num)
    elif num < 0: print("Number is Negative :", num)
    else : print("Zero",num)
positive_or_negative(int(input("Enter the number :")))

