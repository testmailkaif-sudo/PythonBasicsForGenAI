'''*args — Variable Number of Arguments
Accept any number of arguments as a tuple.'''
def total(*args):
    print(args)        # (1, 2, 3, 4, 5) — it's a tuple
    return sum(args)

print(total(1, 2, 3))        # 6
print(total(1, 2, 3, 4, 5))  # 15



'''**kwargs — Keyword Variable Arguments
Accept any number of keyword arguments as a dictionary.'''

def profile(**kwargs):
    print(kwargs)   # {'name': 'Alice', 'age': 15}
    for key, value in kwargs.items():
        print(f"{key}: {value}")

profile(name="Alice", age=15, city="NYC")
# name: Alice
# age: 15
# city: NYC