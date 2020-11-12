class A:
    data = 0

    def printData(self):
        print(self)
        print(self.data)
        
#객체화
obj = A()
obj2 = A()

print(obj)
obj.data = 100
obj.printData()

print(obj2)
obj2.printData()
