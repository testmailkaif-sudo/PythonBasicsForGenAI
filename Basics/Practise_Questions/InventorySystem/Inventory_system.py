'''Build an inventory system:

add_item(inventory, item, quantity, price) → adds or updates item
sell_item(inventory, item, quantity) → reduces quantity, prints error if not enough stock
show_inventory(inventory) → prints all items, quantity, price and total value'''

inventory = {}
def add_iteam(inventory,iteam,quantity,price):
    if iteam in inventory:
        inventory.get(iteam)[0] += quantity
        inventory.get(iteam)[1]=price
        return inventory
    else:
        inventory[iteam]= [quantity,price]
    return inventory
def sell_iteam(inventory,iteam,quantity):
    if quantity > inventory.get(iteam)[0]:
        print("Requested Stock Not available")
    else:
        inventory.get(iteam)[0] -= quantity
        print(quantity, "stocks of ",iteam," are sold" )
def show_inventory(inventory):
    for i,j in inventory.items():
        print(i, " has ",inventory[i][0],"in quantity and price is",inventory[i][1],"total amount of iteam is", inventory[i][0]*inventory[i][1])
print(add_iteam(inventory,"board",10,10))
print(add_iteam(inventory,"board1",10,15))
print(sell_iteam(inventory,"board",10))
show_inventory(inventory)