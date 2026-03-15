'''Problem 4 — Password Validator 🔐
(Functions + Loops + Control Flow + Operators)
Write a function validate_password(password) that checks:

Length must be at least 8 characters
Must contain at least one number
Must contain at least one uppercase letter

Print which rules passed and which failed. Return True if all pass, False otherwise.'''

#Rule 1 → Is length >= 8?
#Rule 2 → Does it have at least one number?
#Rule 3 → Does it have at least one uppercase letter?

def validate_password(password):
    rules_pass = True
    if len(password) <8:
        rules_pass = False
    else:
        rules_pass = True
    is_num = False
    for i in password:
        if i.isdigit():
            is_num= True
            break
    if is_num:
        is_num= True
    else:
        rules_pass = False
    is_upper = False
    for i in password:
        if i.isupper():
            is_upper = True
            break
    if is_upper:
        rules_pass = True
    else:
        rules_pass = False
    return  rules_pass


print(validate_password("hell2"))