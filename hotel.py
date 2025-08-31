# define menu
menu = {
    'Coffee':50,
    'Milk': 25,
    'Tea': 30,
    'Chocolate Milk': 50,
    'Masala Tea': 30,
    'Chaas': 40,
}

# greet
print("Welcome to my restaurant")
print("Menu\nCoffee: 50 Rs\nMilk: 25 Rs\nTea: 30 Rs\nChocolate Milk: 50 Rs\nMasala Tea: 30 Rs\nChaas: 40 Rs")

order_total = 0
# 50 + 30 = 80

item_1 = input("Enter The name of item you want to order?")
if item_1 in menu:
   order_total += menu[item_1]  
   print(f"Your item {item_1} has been added to your order")

else:
   print(f"Your item_1 {item_1} is not in the menu. Please order something else")

   
another_order = input("Do you want to add another item?(Yes/No)")
if another_order == 'Yes':
      
    item_2 = input("Enter the name of second item:")
if item_2 in menu:
      order_total += menu[item_2]
      print(f"The total amount of items to pay is {order_total}")
else:
      print(f"Ordered item {item_2} is not in the list")


    #   print(f"The total amount of items to pay is {order_total}")
