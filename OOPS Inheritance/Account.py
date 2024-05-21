from Bank import Bank

class Account(Bank):
    def __init__(self,name,email,address):
       self.name=name
       self.email=email
       self.address=address

    def set_mobile(self,mobile):
        self.Acc_mobile=mobile
    def get_mobile(self):
        return self.Acc_mobile
    def cal_bal():
        return 0
    def open_account(self):
        print("account opened Successfully")
    
a1=Account('preeti','rahul@gmail.com','delhi')
a1.set_mobile(9988776655)
a1.open_account()
print(a1.get_mobile())
print(a1.__dict__)