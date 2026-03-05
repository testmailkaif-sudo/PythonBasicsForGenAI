print(3 + 2 * 4 ** 2 - 10 // 3)
print(not (5 > 3 and 2 < 1) or 4 == 4)
print(15 & 9)
print(True + True + False + True)


a = True
b = False
c = True
print(a or b and c) # True
print((a or b) and c) #True
print(a and not b or c) #True
print(not (a and b) or not c)#True

#Using only arithmetic and comparison operators (no if, no functions), write an expression that returns 1 if a number is positive, -1 if negative, and 0 if zero.
num = int(input("Enter number :"))

print((num >0)-(num<0))