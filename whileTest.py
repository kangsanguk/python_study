#기타 연산자
#1~10까지 중 4까지만 출력하기
'''
for i in range(10):
    print(i+1)
    if i == 3:
        break

'''

#1~10까지중 4제외하고 출력하기
'''
for i in range(10):
    if i == 3:
            continue
    print(i+1)

'''

#while
'''
cnt = 0
while cnt != 10:
    cnt += 1
    print(str(cnt) + ". 강상욱")

'''

#Q. 다음 중 프로그래밍 언어가 아닌 것은?
#1. JAVA
#2. 파이썬
#3. C언어
#4. 망둥어

msg = "Q. 다음 중 프로그래밍 언어가 아닌 것은?\n1. JAVA\n2. 파이썬\n3. C언어\n4. 망둥어"
print(msg)

while True:
    
    choice = int(input("답 : "))

    if choice == 4:
       msg1 = "정답!!"
    elif choice > 0 and choice < 5:
        msg1 = "오답!"
    else:
        msg1 = "다시 시도해주세요~"

    print(msg1)
    if msg1 == "정답!!":
        break
