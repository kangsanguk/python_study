#가게 상호명 : 문자열
#위치 : 문자열
#메뉴[메뉴명1 : 가격원, 메뉴명2 : 가격원] 문자열
#평수 : 정수
#층고 : 실수
#가게 등급 : 문자
name = "정신차리자"
place = "서울 강서구"
menu1 = "파스타"
price1 = 10000
menu2 = "햄버거"
price2 = 9000
wide = 50
floar = 1.00
denggub = 'A'
print("가게 상호명 : " + name)
print("위치 : %s" %place)
print("메뉴[" + menu1 + " : " + str(price1)  + ", " + menu2 + " : "  + str(price2) + "]")
print("평수 : %d평" %wide)
print("층수 : %.2f" %floar)
print("가게 등급 : %c" %denggub)
