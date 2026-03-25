'''Problem 2 — Email Validator 📧
(Strings + Functions + Loops + Control Flow)
Write a function validate_email(email) that checks:

Must contain exactly one @
Must contain a . after the @
Must not have spaces'''

def email_validator(emailid):
    is_email = True
    for i in range(len(emailid)):
        if emailid[i] == " ":
            is_email = False
            break
    if emailid.find("@") == True:
        if is_email:
            emailid = emailid.split("@")
            for i in emailid:
                if "." in emailid[1]:
                    is_email = True
                else:
                    is_email = False
        else:
            is_email = False
    else:
        is_email = False
    return is_email
print(email_validator("shaikmohammadkaif.spplintron@com"))