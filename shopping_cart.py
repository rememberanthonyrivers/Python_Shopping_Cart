# my shopping cart adds items, removes items, displays items, empty the cart
cart = []


def add_item(item):
    cart.append(item)


def remove_item(item):
    if item in cart:
        cart.remove(item)


def display_cart():
    for item in cart:
        print(item)


def clear_cart():
    cart.clear()
    print("\n\tItems in cart : " + str(len(cart)))


def main():
    while True:
        response = input(
            "\n\tWelcome! What would you like to do? ADD / REMOVE / SHOW / CLEAR / QUIT . enter your option / \n"
        ).lower()

        if response == "quit":
            display_cart()
            print("\n\tThanks for shopping with us ! Come back soon!\n")
            break

        elif response == "add":
            while True:
                item = input(
                    "\n\tWhat item would you like to add to your cart? Enter quit when you are finished. \n"
                )
                if item == "quit":
                    break
                else:
                    add_item(item)
        elif response == "remove":
            item = input(
                "\n\tWhich item would you like to remove ? Enter quit when you are finished. \n"
            )
            if item in cart:
                remove_item(item)
                display_cart()
            else:
                print("\n\tItem not found, Try again .\n")

        elif response == "show":
            if len(cart) == 0:
                print("\n\tYour shopping cart is empty! \n")
            else:
                display_cart()

        elif response == "clear":
            check = input("\n\tARE YOU SURE YOU WANT TO EMPTY YOUR CART?? yes / no \n")
            if check == "yes":
                clear_cart()

        else:
            print("\n\tInvalid response. Try again! \n")


main()
