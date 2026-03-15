'''Check if a username is in the allowed list, print "Access Granted" or "Access Denied"'''
def surname(username):
    surnames = ["Shaik","Podile","Sapa"]
    if username in surnames: print("Access Granted")
    else:print("Access Denied")
surname(str(input("Enter the surname from the list Shaik,Podile,Sapa:")))
