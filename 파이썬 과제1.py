#정보통신공학과 60161850 강상욱 파이썬 1번 과제
str1 = input("문자열 입력 >> ")
s = int(len(str1))
print("참조할 첨자: 0 ~ " + str(s-1))
n = int(input("참조할 첨자 입력 >> "))
print("문자열:" + str1 + ", 길이: " + str(s))
print("참조 문자: " + str1[n])
