'''break Statement
Exits the loop immediately when condition is met.'''

for i in range(1, 10):
    if i == 5:
        break       # stops loop at 5
    print(i)
# 1 2 3 4


# break in while
num = 0
while True:          # infinite loop
    num += 1
    if num == 5:
        break        # exits when num reaches 5
print("Stopped at", num)   # Stopped at 5