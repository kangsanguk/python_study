#정보통신공학과 60161850 강상욱 파이썬 3번 과제

time = input("시간 정보(16:30:15) 입력 >> ")
hour, min, sec = time.split(":")
print("입력 시간 정보: " + hour + ":" + min + ":" + sec)
print(hour + "시 " + min + "분 " + sec + "초")
