#A person can vote if they are 18 or older AND a citizen

def voting_system(age,is_citizen):
    if is_citizen==1 and (age >=18):print("Eligible")
    else:print("Not eligible")
voting_system(int(input("Enter the age :")),int(input("is he a citizen 0-No,1-Yes:")))