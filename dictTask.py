#등급을 입력하면 학점을 알려주는 프로그램
#1~5등급
#A~F학점(E제외)
#dict로 구현하기

gradeDict = {}
temp = 0
for i in range(5):
    temp = i
    if i == 4:
        temp += 1
    if i+1 not in gradeDict:
        gradeDict[i+1] = chr(temp+65)

#print(gradeDict)
print(gradeDict[int(input("등급 : "))] + "학점입니다.")
