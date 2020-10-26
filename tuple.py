'''
arData = [1, 2, 3]
copy_arData = arData

copy_arData.append(4)

print(arData)

'''

dataTuple = 1, 2, 3
copy_dataTuple = dataTuple

copy_dataTuple += (4, 5)

print(dataTuple)
print(copy_dataTuple)
print(dataTuple[0])

for i in copy_dataTuple:
    print(i)

#주석은 모두 오료(tuple에서 지원하지 않는 문법)
#del copy_dataTuple[0]
#copy_dataTuple.remove(1)
#dataTuple[0] = 10

