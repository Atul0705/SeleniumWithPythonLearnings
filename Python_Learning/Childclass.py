from SeleniumWithPython.Python_Learning.ForLoop import Calculator


class ChildImp(Calculator):
    num2 = 100

    def __init__(self):
        Calculator.__init__(self, 2, 10)

    def getcompletedata(self):
        return self.num + self.num2 + self.summation()


obj = ChildImp()
print(obj.getcompletedata())
