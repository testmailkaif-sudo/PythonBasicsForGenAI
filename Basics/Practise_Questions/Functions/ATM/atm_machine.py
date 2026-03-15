total_balance = 1000
def balance ():
    return total_balance
def deposit(amount):
    total= balance()
    total+= amount
    return total
def withdrawal(amount):
    total = balance()
    if amount > total:
        print("Invalid Input")
    else :
        total -= amount
    return total
print(balance())
print(deposit(100))
print(withdrawal(200))