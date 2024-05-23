from sa import *
from ca import *

def get_service(obj):
    print(obj.cal_bal())

    sa1=SA(101,'Rahul','rahul@gmail.com','delhi',5000)
    ca1=CA(101,'Shruti','shruti@gmail.com','Skt',5000)
    a1=Account('Preeti','preeti2Gmail.com','Banglor')
get_service(sa1)
get_service(ca1)
get_service(Account)

