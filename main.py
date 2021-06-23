shopping_list2 = []

print(shopping_list2)

def shopping_cart2(groceries):

    for items in groceries.split(" "):

        shopping_list2.append(items) #(input("What fruit would you like to put in ? "))
        print(shopping_list2)

shopping_cart2("apple")
shopping_cart2("banana")
shopping_cart2("lemon")
shopping_cart2("kiwi")
shopping_cart2("dragon fruit")
shopping_cart2("peach")
shopping_cart2("pineapple")
shopping_cart2("strawberry")
shopping_cart2("blueberry")
shopping_cart2("blackcurrent")
shopping_cart2("cranberry")

del(shopping_list2[0])

print(shopping_list2)

shopping_list2.clear()

print(shopping_list2)


