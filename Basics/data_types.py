#Numeric Data Types
x = 10          # int   – whole numbers
y = 3.14        # float – decimal numbers
z = 2 + 3j      # complex – real + imaginary
#String - Charactes
name = "Hello, World!"
#Boolean Data Types
is_valid = True
is_empty = False
#Sequence Types - List, Tuple, range
#List - ordered, mutable, allows duplicate
fruits = ["apple", "banana", "cherry","apple"]
#Tuple - ordered, immutable - Tuples once created cannot be modified.
product = ('Microsoft', 'Xbox', 499.99)
#Range - Immutable, most commonly used for looping
x1 = range(5) #need to convert to list to execute
list(x1)


#Mapping Data Types - Dictionary
person = {"name": "Alice", "age": 30} #key-value pairs
# Set Types - Set, frozenset
#A set is a collection of unique data, meaning that elements within a set cannot be duplicated.
student_id = {112, 114, 116, 118, 115}
# Frozen set is an immutable (unchangeable) version of a standard Set.
my_list = [1, 2, 3, 2, 1]
frozen_set = frozenset(my_list) #[1,2,3]
# Boolean - True, False
#None Data Type