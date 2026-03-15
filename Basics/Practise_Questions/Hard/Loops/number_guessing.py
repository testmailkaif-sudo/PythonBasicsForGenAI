'''Using a while loop, write a number guessing game:

Secret number is 42
User keeps guessing until correct
Print "Too High", "Too Low", or "Correct!"'''

while True:
    number = int(input("Enter the number : "))
    while number != 42:
        if number > 42:
            print("Too High")
            break
        elif number < 42:
            print("Too Low")
            break
    else:
        print("Correct")
        break

for i in range(3):
    for j in range(3):
        if j == 1:
            break
    else:
        print("inner else:", i)
else:
    print("outer else")
num = int(input("Enter the number : "))
for i in range (1,num+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()