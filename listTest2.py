#1. [값]*길이
#2. [값1, 값2, ...]
#[] --> append()
#arData = [3,4,5,6,7]
#print(6 not in arData)
#print(3 in arData)

#for i in arData:
    #print(i)

arData = [0] * 5

#추가
#1부터 10까지 중 짝수만 넣고 100 따로 추가하기

for i in range(len(arData)):
    arData[i] = (i+1)*2
print(arData)

#2뒤에 3넣기

if 2 in arData:
    arData.insert(arData.index(2),3)
else:
    print("값이 존재하지 않습니다.")
#print(arData)

#수정
#4를 5로 수정하기

if 4 in arData:
    arData[arData.index(4)] = 5
else:
    print("값이 존재하지 않습니다.")
print(arData)

#삭제
#10삭제하기

if 10 in arData:
    arData.remove(10)
else:
    print("값이 존재하지 않습니다.")
print(arData)

#1번째 방 삭제하기

if len(arData) > 1 :
    del arData[1]
else:
    print("값이 존재하지 않습니다.")
print(arData)

#검색
#6검색 하고 인덱스 출력하기

if 6 in arData:
    print("index : %d" %arData.index(6))
else:
    print("값이 존재하지 않습니다.")

#목록
#list에 있는 모든 값 출력하기
for i in arData:
    print(i)
#검사
#7이 있는지 확인 후 있으면 7이 존재한다고 출력
#없으면 없다고 출력
