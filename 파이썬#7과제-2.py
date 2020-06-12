import bloodPressure
import time
import datetime

for i in range(1, 4):
    max, min = bloodPressure.bpInput()
    d = datetime.datetime.now()
    print(str(d.year)+"년 "+str(d.month)+"월 "+str(d.day)+"일 "+str(d.hour)+"시 "
          +str(d.minute)+"분 혈압 "+str(max)+"/"+str(min))
    avg1, avg2 = bloodPressure.dbCalc(max, min)
    print("지난 " + str(i) + "회 동안의 평균 혈압 " + str(avg1) + "/" + str(avg2))
    time.sleep(60)
