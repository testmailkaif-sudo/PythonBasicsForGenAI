'''A Caesar cipher shifts each letter by a fixed number.
Write a function caesar_cipher(text, shift) that:

Shifts each letter forward by shift positions
Leaves non-letters (spaces, numbers) unchanged
Wraps around — after z comes a'''


def caesar_cipher(name, shift_count):
    f_name = ""
    if shift_count ==0:
        print("Invalid Input !")
    else:
        for i in name:
            if 97 <= ord(i) <= 122 or 65 <= ord(i) <=90:
                count = ord(i) + shift_count
                j = chr(count)
                f_name += j
            else:
                f_name+=i
        print(f_name)
caesar_cipher("Hello World",3)