import time
now = time.localtime()
print("현재 시간은 ", time.asctime())
print(now.tm_mon,"월")

if (now.tm_hour < 11) :
    print("Good Morning!")
elif (now.tm_hour < 15) :
    print("Good Afternoon!")
elif (now.tm_hour < 20 ) :
    print("Good Evening!")
else :
    print("Good Night!")

if(now.tm_year % 4 == 0 and now.tm_year % 100 != 0 or now.tm_year % 400 == 0) :
    print("올해는", now.tm_year,"년이고 윤년 입니다.")
else :
    print("올해는", now.tm_year,"년이고 윤년이 아닙니다.")
