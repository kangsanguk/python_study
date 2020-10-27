cafeDict = {"아메리카노" : 3000, "카페라떼" : 4000}
print(type(cafeDict))

print(cafeDict)

if "샌드위치" not in cafeDict:
    #추가
    cafeDict["샌드위치"] = 5007
    msg = "추가"
else:
    #수정
    cafeDict["샌드위치"] = 5000
    msg = "삭제"
print(msg + "\n" + str(cafeDict))

'''
del cafeDict["카페라떼"]

for i in cafeDict.keys():
    print(i)

'''

arPrice = list(cafeDict.values())
total = 0
avg = 0.0

for i in range(len(arPrice)):
    total += arPrice[i]

avg = "%.2f" %(total / len(cafeDict))
print("총 가격 %d원" %total)
print("평균 가격 " + avg + "원")
