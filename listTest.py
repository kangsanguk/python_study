#arData = [1, 2, 3, 4]
#맨 뒤 추가
arData.append(5)

arData[0] = 10

#원하는 곳에 추가(삽입)
arData.insert(1, 9)

#삭제(인덱스)
del arData[0]

#삭제(값)
arData.remove(5)

#검색
print(arData.index(4))

#arData = [0] * 4

#for i in range(len(arData)):
    #arData[i] = i+1
#arData = []

#for i in range(4):
    #arData.append(i+1)
'''
arData.append(1)
arData.append(2)
arData.append(3)
arData.append(4)

'''

print(arData)
#print(arData._str_())
