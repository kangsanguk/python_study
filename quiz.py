#Q. 다음 중 프로그래밍 언어가 아닌 것은?
#1. JAVA
#2. 파이썬
#3. C언어
#4. 망둥어

msg1 = "Q. 다음 중 프로그래밍 언어가 아닌 것은?"
msg2 = "1. JAVA"
msg3 = "2. 파이썬"
msg4 = "3. C언어"
msg5 = "4. 망둥어"
print(msg1)
print(msg2)
print(msg3)
print(msg4)
print(msg5)

choice = int(input("답 : "))
result = "정답!!" if choice == 4 else \
         "다시 시도해주세요~" if (choice > 4 or choice < 0) else "오답!"
print(result)
