'''What are Loops?
Loops let your program repeat code multiple times without writing it again and again.
Python has 2 types of loops:

for — repeat a fixed number of times
while — repeat as long as a condition is True

1. for Loop
Used to iterate over a sequence (list, string, range, etc.)
2. while Loop
Runs as long as the condition is True
'''


#basic For Loop
for i in range(5):
    print(i)# Output: 0 1 2 3 4
#Here the purpose of range function is to generate the sequence of numbers
#range(start,end,diff)
range(5)        # 0, 1, 2, 3, 4
range(1, 6)     # 1, 2, 3, 4, 5
range(0, 10, 2) # 0, 2, 4, 6, 8  ← step of 2
range(10, 0, -1)# 10, 9, 8 ... 1 ← countdown

for i in range(1, 6):
    print(i)   # 1 2 3 4 5

for i in range(0, 10, 2):
    print(i)   # 0 2 4 6 8


'''We can also use for loop over a List/String '''

# Loop over a list
fruits = ["apple", "banana", "mango"]
for fruit in fruits:
    print(fruit)
# apple, banana, mango

# Loop over a string
for char in "Python":
    print(char)
# P y t h o n


