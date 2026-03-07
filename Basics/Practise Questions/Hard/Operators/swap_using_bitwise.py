#Using only bitwise operators, swap two numbers without a temp variable:
def swap(num1,num2):
    print("original",num1,num2)
    num1 ^= num2
    num2 ^= num1
    num1 ^= num2
    print(num1,num2)
swap(5,6)