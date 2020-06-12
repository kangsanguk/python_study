money = int(input("예금 원금: "))
rate = 0.05

def getinterest(money, rate, year):
    total = money*((1+rate)**year)
    print("%d년 총액: %.2f" %(year, total))
    
for year in [2, 4, 6, 8]:
    getinterest(money, rate, year)
