class Employee:
    org_name='TCS'

    def set_ename(self,ename):
        self.ename=ename
    def set_esal(self,esal):
        self.esal=esal
e1=Employee()
e1.set_ename('preeti')
e1.set_esal(45000)

e2=Employee()
e2.set_ename('shruti')
e2.set_esal(500000)

print(e1.__dict__)
print(e2.__dict__)