class Customer:
    
    def setCustomername(self,customername): #setter
        self.customername=customername

    def setCustaddress(self,custaddress): #setter
        self.custaddress=custaddress

    def setCustdob(self,custdob):   #setter
        self.custdob=custdob
        
    def getCustomername(self):
        return self.customername
    
    def getCustaddress(self):
        return self.custaddress

    def getCustdob(self):
        return self.custdob
    
   
    


class Employ:

    def setEmployname(self,employname): #setter
        self.employname=employname

    def setEmployid(self,employid): #setter
        self.employid=employid

    def setEmploydob(self,employdob): #setter
        self.employdob=employdob
    def getEmployname(self):
        return self.employname
    def getEmployid(self):
        return self.employid
    def getEmploydob(self):
        return self.employdob
    
    

#getters
    



cst=Customer()
cst.setCustomername("hazik")
cst.setCustaddress("bemina")
cst.setCustdob("19/11/1998")
emp=Employ()
emp.setEmployname("raj")
emp.setEmployid("aud9739")
emp.setEmploydob("12/11/1998")

print (cst.getCustomername())
print (cst.getCustaddress())
print (cst.getCustdob())
print (emp.getEmployname())
print (emp.getEmployid())
print (emp.getEmploydob())

