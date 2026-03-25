'''Problem 1 — Username Formatter 👤
(Strings + Functions + Control Flow)
Write a function format_username(full_name) that:

Removes extra spaces from both ends
Converts to lowercase
Replaces spaces between words with _
Returns the formatted username'''

def format_username(full_name):
    full_name = full_name.strip()
    print(full_name)
    full_name = full_name.lower()
    print(full_name)
    full_name = full_name.replace(" ","_")
    print(full_name)
    return full_name
print(format_username("   Shaik Podile Mohammad Kaif   "))