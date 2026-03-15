'''A bank allows withdrawal only if account is active, balance is enough,
 and amount is greater than 0. Print success or the exact reason it failed.'''

def withdrawal(total_balance,withrawal_amount):
    if total_balance > withrawal_amount:
        print("withrawal of",withrawal_amount," is successful and your current balance is ",total_balance-withrawal_amount)
    else:
        print("Your amount withdrawal amount greater than the account balance")
withdrawal(int(input("Enter the total ammount : ")),int(input("Enter the Withdrawal amount : ")))