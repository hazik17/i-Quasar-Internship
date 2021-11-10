class Billing:
    GT=0
    def __init__(self):
         pass
        
    def generate_bill(self,cart):
        for item in cart:
            self.GT=self.GT+item.getPrice()
        
        self.display_bill(cart,self.GT)
        
    def display_bill(self,cart,GT):
        print("ITEM NAME\t\tPRICE")
        for item in cart:
            print(item.getItemname(),"\t\t",item.getPrice())
        print("\t________________________________________")
        print("\tGrand TOtal=\t",GT)
        

