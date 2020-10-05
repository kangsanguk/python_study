#Q. 다음 중 프로그래밍 언어가 아닌 것은?
#1. JAVA
#2. 파이썬
#3. C언어
#4. 망둥어

msg = "Q. 다음 중 프로그래밍 언어가 아닌 것은?\n1. JAVA\n2. 파이썬\n3. C언어\n4. 망둥어"
print(msg)

choice = int(input("답 : "))

if choice == 4:
   msg1 = "정답!!"
elif choice > 0 and choice < 5:
    msg1 = "오답!"
else:
    msg1 = "다시 시도해주세요~"

print(msg1)
