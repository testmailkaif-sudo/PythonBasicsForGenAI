'''. Given a = 15 and b = 4, print the result of all 7 arithmetic operators.'''
def result_arthematic_operators(num1,num2):
    print("Addition =",num1+num2)
    print("Subtration : ", num1-num2)
    print("Multipication : ", num1 * num2)
    print("Division : ",num1/num2)
    print("Modulos :", num1%num2)
    print("Exponential :", num1**num2)
    print("Floor division : ",num1//num2)
result_arthematic_operators(int(input("Enter the first number1 :")),int(input("Enter the first number2 :")))