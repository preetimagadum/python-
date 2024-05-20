class Test:
    a=10

    def m1(self,b):
        self.b=b
        
    def m2(self,c):
        self.c=c
    def m3(self,d):
        self.d=d
t1=Test()
t1.m1(20)

t2=Test()
t2.m2(30)

t3=Test()
t3.m3(40)

print(t1.__dict__)
print(t2.__dict__)
print(t3.__dict__)