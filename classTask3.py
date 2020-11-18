#동물 클래스
#이름, 체력, 먹이이름, 먹이갯수

#먹기 : 체력 1증가 먹이 1감소
#자기 : 3초당 체력 1증가
#산책하기 : 체력 1감소,
#랜덤한 문제출제 후 정답시 먹이 2증가 오답시 체력 1감소

import random as r

class Animal:

    quizDict = {"Q. 다음중 동물이 아닌 것은?\n1.돼지\n2.고양이\n3.구름\n4.강아지\n" : 3, \
                "Q.코로나 예방 수칙중 잘못된것은?"\
                "\n1.자주 손씻기\n2.얼굴 만지기\n3.마스크 쓰기\n4.야외활동 자제하기\n" : 2, \
                "Q. 1+3 = ?\n1. 1\n2. 2\n3. 3\n4. 4\n" : 4}
    
    def __init__(self, name, health, foodName, foodCount):
        self.name = name
        self.health = health
        self.foodName = foodName
        self.foodCount = foodCount

    def eat(self):
        if self.foodCount == 0:
            print("음식이 부족합니다! 산책 다녀오세요~")

        else:
            self.health += 1
            self.foodCount -= 1
            print(self.name + "이(가)" + foodName + "먹는중..")
            print("현재 체력 : %d\n남은 먹이 갯수 : %d개" %(self.health, self.foodCount))


    
    def walk(self):
        if self.health == 1:
            print("체력이 부족합니다!")

        else:
            self.health -= 1
            idx = r.randrange(0, len(Animal.quizDict))
            quiz = list(Animal.quizDict.keys())[idx]
            choice = int(input(quiz))

            if Animal.quizDict[quiz] == choice:
                print("정답!!")
                self.foodCount += 2
            else:
                self.health -= 1
                if self.health == 0:
                    print("회복중...")
                    self.sleep()
                else:
                    print("오답ㅜㅜ")
                    
        def sleep(self):
            pass

dog = Animal('이름', 1, '먹이',10)
dog.walk()

