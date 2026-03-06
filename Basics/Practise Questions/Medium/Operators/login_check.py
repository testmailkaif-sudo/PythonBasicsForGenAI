def login_check(username,password,is_active):
    dict1 = {"kaif":"Kaif@123"}
    if username in dict1 and password == dict1[username] and is_active == 1:print("Login Success")
    else: print("Invalid Credentials")
login_check("kaif","Kaif@123",1)