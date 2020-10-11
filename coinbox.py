#동전노래방
#1. 돈 넣기
#2. 노래 재생

#1. 500원(2곡)
#2. 1000원(5곡)

#노래재생시 랜덤한 점수(10점 단위)
#100점시 코인 1개 서비스
import time
import random as r
msg = "동전노래방\n1. 돈 넣기\n2. 노래재생\n3. 나가기\n"
coinMsg = "1. 500원(2곡)\n2. 1000원(5곡)\n3. 취소"
errMsg = "다시 시도해주세요"

score_100Msg = "훌륭합니다. 가수신가요?"
score_50Msg = "조금만 노력하면 가수도 문제 없어요!"
score_0Msg = "연습을 많이 하셔야겠어요~ㅠㅠ"

choice = 0
coin = 0
money = 10000

score = 0
song_2 = 500
song_5 = 1000

while True:
    choice = int(input(msg + "코인:" + str(coin) + "개\n"))
    #돈 넣기
    if choice == 1:
        #변수의 재사용
        #1. 메모리 효율적
        #2. 가독성이 떨어진다
        choice = int(input(coinMsg))

        #500원
        if choice == 1:
            #잔액 부족
            if money - song_2 < 0:
                print(errMsg + " / 잔액부족\n")
            else:
                #사용자 돈에서 song_5의 가격만큼 빼주기
                money -= song_5
                coin += 2

        #1000원
        elif choice == 2:
            if money - song_5 < 0:
                print(errMsg + " / 잔액부족\n")
            else:
                 #사용자 돈에서 song_2의 가격만큼 빼주기
                money -= song_2
                coin += 2
                
        #메인화면으로 이동
        elif choice == 3:
            pass
        else:
            print(errMsg + "\n")
            
    #노래재생
    elif choice == 2:
        #코인이 0개이면
        if coin < 1:
            print("코인이 부족합니다.")
            #밑의 문장을 하지 않고 메인화면으로 이동
            continue

        #코인이 있다면 1개 감소
        coin -= 1

        #3초에 한곡씩 재생
        print("재생중", end = '')

        for i in range(3):
            print(".", end = '')
            
            #1초 멈춤
            time.sleep(0.1)

        #줄바꿈
        print()
        #점수(100, 90, 80, 70, 60, 50, 40, 30)
        #3~10중 랜덤한 값 * 10
        score = r.randrange(3, 11) * 10
        print(str(score) + "점!")
        if score > 70:
            #100점이면
            if score == 100:
                #한 곡 보너스
                coin += 1
            print(score_100Msg)
        elif score > 40:
            print(score_50Msg)
        else:
            print(score_0Msg)

    #나가기
    elif choice == 3:
        break
    
    else:
            print(errMsg + "\n")
