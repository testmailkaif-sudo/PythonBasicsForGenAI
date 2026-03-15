cart ={}
def add_items(cart,item,price,quantity=1):
    cart[item] = {"price":price,"quantity":quantity}
    return cart
def show_cart(cart):
    for item, details in cart.items():
        print(item)
        print(details)
        print(details["price"])
        print(details["quantity"])
def cart_discount(cart,discount):
    total_amount =0
    for item, details in cart.items():
        total_amount += details["price"]*details["quantity"]
    total_amount = total_amount - (total_amount*(discount/100))
    return  total_amount
cart = add_items(cart,"Apple", 10, 4)
cart = add_items(cart,"Orange", 10, 4)

print(cart_discount(cart,10))
show_cart(cart)