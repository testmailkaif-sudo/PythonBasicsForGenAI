'''Build a traffic light system two ways — once with if/elif/else, once with ternary:'''

def traffic_light (signal):
    if signal == 'Yellow':
        print("Get Ready")
    elif signal == 'Red':
        print("Stop")
    elif signal == 'Green':
        print("Go")
    else:
        print("Invalid")
traffic_light(str(input("Enter the Signal : ")))
''' Predict the output without running and explain why'''

x = 0
y = 10
z = ""

if x or y:
    print("A")
if x and y:
    print("B")
if not z:
    print("C")
if x or not z:
    print("D")