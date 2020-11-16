#자동차 클래스 만들기
#클래스 이름은 Car이고
#필드의 객체는 brand, color가 있다.
#메소드는 engineStart(), engineStop()이 있다.
#엄마차와 아빠차 객체 2개를 만들고
#각각 시동을 켜면 엄마차는 Benz(Black) 시동 켜짐,
#아빠차는 BMW(Blue) 시동 켜짐으로 출력하기

class Car:
    brand = ''
    color = ''

    def engineStart(self):
        print(self.brand + "(" + self.color + ") 시동켜짐")

    def engineStop(self):
        print(self.brand + "(" + self.color + ") 시동켜짐")

momCar = Car()
dadCar = Car()

momCar.brand = "Benz"
momCar.color = "Black"

dadCar.brand = "BMW"
dadCar.color = "Blue"

momCar.engineStart()
momCar.engineStop()

dadCar.engineStart()
dadCar.engineStop()

