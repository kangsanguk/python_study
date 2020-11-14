#생성자
class Car:

    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
        
    def engineStart(self):
        print(self.brand + "(" + self.color + ") 시동켜짐")

    def engineStop(slef):
        print(self.brand + "(" + self.color + ") 시동켜짐")

momCar = Car('Benz', 'Black')
momCar.engineStart()
