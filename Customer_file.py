class Customer:
    custname=""
    custid=0

    def __init__(self,custname,custid):
        self.custname=custname
        self.custid=custid

    def getCustname(self):
        return self.custname
    def getCustid(self):
        return self.custid
