#Arthematic Operators
a, b = 10, 3
print(a + b)   # 13
print(a - b)   # 7
print(a * b)   # 30
print(a / b)   # 3.333...
print(a // b)  # 3  ← removes decimal
print(a % b)   # 1  ← remainder
print(a ** b)  # 1000

# Comparision Operators
age = 18
print(age == 18)   # True
print(age > 21)    # False
print(age < 21)    #True
print(age >= 18)   # True
print(age <= 18)   # True
print(age != 10)   # True

# Logical Operators
a, b = 10, 5
print(a > 5 and b < 3)   # False
print(a > 5 or b < 3)    # True
print(not (a > 5))       # False

#Assignment Operators
x = 10
x += 5    # x = 15
x -= 3    # x = 12
x *= 2    # x = 24
x /= 4    # x = 6.0   (becomes float)
x //= 2   # x = 3
x **= 3   # x = 27
x %= 5    # x = 2
print(x)

#Bitwise Operators
a, b = 5, 3   # a=0101, b=0011 (binary)
print(a & b)   # 1  (0001)  AND
print(a | b)   # 7  (0111)  OR
print(a ^ b)   # 6  (0110)  XOR
print(~a)      # -6 (bitwise NOT; two's complement)
print(a << 1)  # 10 (1010)  left shift
print(a >> 1)  # 2  (0010)  right shift

#Membership Operators - in, not in
nums = [1, 2, 3]
print(2 in nums)         # True
print(4 not in nums)     # True
text = "hello"
print("he" in text)      # True
print("z" not in text)   # True
d = {"a": 1, "b": 2}
print("a" in d)          # True (checks keys)
print(1 in d.values())   # True (explicitly check values)


#Identity Operators - is, is not
a = [1, 2, 3]
b = a          # b points to same list
c = [1, 2, 3]  # c is a new list

print(a is b)      # True  ← same object
print(a is c)      # False ← different objects
print(a == c)      # True  ← same value
print(a is not c)  # True