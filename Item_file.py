class Item:
    itemname=""
    price=0

    def __init__(self,itemname,price):
        self.itemname=itemname
        self.price=price
    
    def getItemname(self):
        return self.itemname


    
    def getPrice(self):
        return self.pricewhile
    print("Item ID \tItem Name\t\tItem Price")
    print("1 Lays\t\t\t 130")
    print("2 Choco\t\t\t 230")
    print("3 Biscuit\t\t\t 330")
    print("4 Soda\t\t\t 350")
    print("5 Candies\t\t\t 130")
    print("6 Cola\t\t\t 240")
    cart=0
    item_choice=input("Enter Item Id")

    if item_choice=="1":
        cart.append(Item("Lays",130))
    if item_choice=="2":
        cart.append(Item("Choice",230))
    if item_choice=="3":
        cart.append(Item("Buscuit",330))
    if item_choice=="4":
        cart.append(item("Soda",330))
    if item_choice=="5":
        cart.append(Item("Candies",130))
    if item_choice=="6":
        cart.append(Item("Cola",240))
        
        
