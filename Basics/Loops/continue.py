'''. continue Statement
Skips current iteration and moves to the next one.'''


for i in range(1, 6):
    if i == 3:
        continue    # skips 3
    print(i)
# 1 2 4 5


# continue in while
num = 0
while num < 6:
    num += 1
    if num == 3:
        continue     # skips printing 3
    print(num)
# 1 2 4 5 6
