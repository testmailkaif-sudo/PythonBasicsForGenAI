'''Print the multiplication table of any number using a for loop:'''

def multiplication(num,range_num):
    for i in range(1,range_num+1):
        print(num," X ",i," = ",num*i)
multiplication(int(input("Enter the number : ")),int(input("Enter the range of multiplication : ")))

# 7 x 1 = 7
# 7 x 2 = 14 ... up to 7 x 10 = 70