'''Else with For Loop

Runs after the loop finishes — only if loop was NOT brok
'''


for i in range(1, 4):
    print(i)
else:
    print("Loop finished!")   # runs after loop ends
# 1 2 3 Loop finished!
print('*******************************************')
# With break — else does NOT run
for i in range(1, 4):
    if i == 2:
        break
else:
    print("This won't print")  # skipped because of break