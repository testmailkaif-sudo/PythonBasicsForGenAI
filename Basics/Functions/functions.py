'''A function is a reusable block of code that runs only when called. Instead of writing the same code again and again, you wrap it in a function and call it whenever needed.'''
#. Defining and Calling a Function
'''def → keyword to define a function
greet → function name
() → parentheses (parameters go here)
: → colon to start the block'''
# Define
def greet():
    print("Hello, World!")
# Call
greet()   # Hello, World!

# Parameters and Arguments

'''Parameters — variables listed in function definition
Arguments — actual values passed when calling'''
def greet(name):         # 'name' is a parameter
    print("Hello", name)

greet("Alice")           # 'Alice' is an argument
greet("Bob")
# Hello Alice
# Hello Bob


#Multiple Parameters

def add(a, b):
    print(a + b)

add(3, 5)    # 8
add(10, 20)  # 30

#return Statement
'''Send a value back to the caller instead of just printing.
return exits the function immediately — any code after it won't run.'''
# print — just displays, can't reuse the value
def add(a, b):
    print(a + b)

# return — sends value back, can reuse it ✅
def add(a, b):
    return a + b

result = add(3, 5)
print(result)        # 8
print(result * 2)    # 16  ← can reuse!


