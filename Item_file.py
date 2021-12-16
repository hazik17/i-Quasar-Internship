class Item:
    itemname=""
    price=0

    def __init__(self,itemname,price):
        self.itemname=itemname
        self.price=price
    
    def getItemname(self):
        return self.itemname


    
    def getPrice(self):
        return self.price
