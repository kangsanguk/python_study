class Car:

    #외부에서 전달될 값이 명확하지 않을 때에는
    #생성자의 매개변수에 초기값을 넣어놓는다.
    #만약 값이 들어오지 않으면 초기값이 들어가고
    #값이 들어오면 들어온 값으로 초기화된다.
    #초기값을 넣어줄 변수들은 뒤에 선언해 주어야 한다.
    #ex) self, color = 'Black', brand : 의미가 없음
    def __init__(self, brand, color = 'Black'):
        self.brand = brand
        self.color = color
        self.checkStart = False
        self.checkStop = False
        
    def engineStart(self):
        if self.checkStart == False:
            print(self.brand + " 시동 킴")
            self.checkStart = True
        else:
            print(self.brand + " 이미 시동 켜져 있음")
    def engineStop(self):
        if self.checkStop == False:
            print(self.brand + " 시동 끔")
            self.checkStop = True
        else:
             print(self.brand + " 이미 시동 꺼져 있음")

#시동이 이미 켜져있거나 꺼져있으면 경고메세지 출력
myCar = Car('Benz')
myCar.engineStart()
myCar.engineStart()
myCar.engineStart()
print("==================")
myCar.engineStop()
myCar.engineStop()
myCar.engineStop()
