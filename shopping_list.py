shopping_list = []

print(shopping_list)

def shopping_cart(groceries):

    for items in groceries.split(" "):

        shopping_list.append(items)
        print(shopping_list)

shopping_cart("apple")
shopping_cart("banana")
shopping_cart("lemon")
shopping_cart("kiwi")
shopping_cart("dragon fruit")
shopping_cart("peach")
shopping_cart("pineapple")
shopping_cart("strawberry")
shopping_cart("blueberry")
shopping_cart("blackcurrent")
shopping_cart("cranberry")

del(shopping_list[0])

print(shopping_list)

shopping_list.clear()

print(shopping_list)


