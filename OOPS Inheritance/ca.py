from Account import *

class CA(Account):
    min_bal=500
    def __init__(self,id,name,email,address,amount):
        super().__init__(name,email,address)
        self.id=id
        self.acc_bal=amount
    def cal_bal(self):
        return self.acc_bal-CA.min_bal

ca1=CA(101,'Shruti','shruti@gmail.com','Skt',5000)
ca1.set_mobile(9988665488)
print(ca1.get_mobile())
print(ca1.cal_bal())
