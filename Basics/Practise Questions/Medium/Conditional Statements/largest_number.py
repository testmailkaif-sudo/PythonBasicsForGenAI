'''Print the largest of three numbers without any built-in functions.'''

def largest_number(a,b,c):
    if a> b and a >c :
        print("A is greater")
    elif a < b and  b >c :
        print(" B ism greater")
    elif a<c and b < c:
        print("C is greater")
largest_number(int(input(" Enter 1st number A :")),int(input(" Enter 1st number B :")),int(input(" Enter 1st number C :")))