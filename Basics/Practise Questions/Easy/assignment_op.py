#. Given x = 100, use assignment operators to:

#Add 50, then multiply by 2, then subtract 30, then divide by 5. Print final value.
def assignment_op(num):
    num+=50;num*=2;num -=30;num /=5;print(num)
assignment_op(int(input("Enter the number :")))