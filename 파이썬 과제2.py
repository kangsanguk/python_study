#정보통신공학과 60161850 강상욱 파이썬 2번 과제
str1 = input("다섯 문자 이상의 문자열 입력 >> ")
print("입력 문자열: " + str1[:])
print("첫 문자: " + str1[:1])
print("마지막 문자: " + str1[-1:])
print("첫 문자를 제외한 부분 문자열: " + str1[1:])
print("마지막 문자를 제외한 부분 문자열: " + str1[:-1])
print("맨 앞과 뒤의 두 문자씩을 제외한 부분 문자열: " + str1[2:-2])
print("문자 하나씩을 건너 뛴 부분 문자열: " + str1[::2])
print("역 문자열: " + str1[::-1])
