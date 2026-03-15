'''A theme park has these rules to ride a rollercoaster:

Height must be above 140 cm
Age must be between 10 and 60 (inclusive)
Must not have a heart condition

Using only operators (no if statements), write a single expression that returns True if someone can ride.'''

def rollercoster(height,age,heart_condition):
    print(height>140 and age in range(10,60) and heart_condition==1)
rollercoster(142,24,1)
