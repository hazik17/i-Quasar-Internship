from Item_file import Item
from Billing_file import Billing

class Shopping:
    def __init__(self):

        while  

        print("Item ID \tItem Name\t\t Item Price")
        print("1 Lays \t\t\t 130")
        print("2 Choco \t\t\t 230")
        print("3 Biscuit \t\t\t 330")
        print("4 Soda \t\t\t 350")
        print("5 Candies \t\t\t 130")
        print("6 Cola \t\t\t 240")
        cart=[]
        item_choice=input("Enter Item Id")

        if item_choice=="1":
            cart.append(Item("Lays",130))
        if item_choice=="2":
            cart.append(Item("Choco",230))
        if item_choice=="3":
            cart.append(Item("Biscuit",330))
        if item_choice=="4":
            cart.append(Item("Soda",350))
        if item_choice=="5":
            cart.append(Item("Candies",130))
        if item_choice=="6":
            cart.append(Item("Cola",240))




        
        
        cart=[it1,it2,it3,it4,it5,it6]
        bl=Billing()
        bl.generate_bill(cart)

