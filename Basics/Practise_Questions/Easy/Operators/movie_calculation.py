''' A movie ticket costs $12. You have $50. Using operators, find out:

How many tickets can you buy?
How much money is left?'''

def balance_calculation(total,ticket):
    print("Total number of tickets you can purchase are :", total//ticket)
    print("Balance amount you will have is ", total%ticket)
balance_calculation(int(input("Enter the total amount :")),int(input("Enter one ticket price :")))