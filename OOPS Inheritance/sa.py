from Account import *

class SA:
    min_bal=500
    def __init__(self,id,name,email,address,amount):
        super().__init__(name,email,address)
        self.acc_id=id
        self.acc_bal=amount
    
    def cal_bal(self):
        return self.acc_bal
    
sa1=SA(101,'Rahul','rahul@gmail.com','delhi',5000)
sa1.set_mobile(9988776655)
print(sa1.get_bal())
print(sa1.cal_bal())