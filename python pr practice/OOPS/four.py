class Employee:
    org_name='TCS'

    def set_ename(self):
        self.ename='preeti'
    def set_esal(self):
        self.esal=88999
e1=Employee()
e1.set_ename()
e1.set_esal()

'''e2=Employee()
e2.set_ename('shruti')
e2.set_esal(500000)'''

print(e1.__dict__)
#print(e2.__dict__)