"""Self keyword is mandatory when creating constructor in py
"""
class Calculator:
    num = 100

    def __init__(self, a, b):
        self.fno = a
        self.sno = b

    def getdata(self):
        print("Iam executing in the class")

    def summation(self):
        return self.fno + self.sno + Calculator.num


obj = Calculator(3,4)
obj.getdata()
print(obj.summation())

obj1 = Calculator(7, 9)
obj1.getdata()
print(obj1.summation())
