class Test:

    def m1(self):
        self.a=100
    @classmethod
    def m2(cls):
        cls.b=200
    @staticmethod
    def m3():
        c=300

t1=Test()
t1.m1()
t1.m2()
t1.m3()

print(t1.__dict__)
print(Test.__dict__)
