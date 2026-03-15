''' Write a program that keeps asking the user for a number until they enter 0, then print the total sum.'''
sum =0
while True:
    num = int(input())
    sum+=num
    if num == 0:
        break
print(sum)