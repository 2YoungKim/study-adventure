x = 3
y = x ** 3 + 3 * x ** 2 + 7 * x + 10

print(y)

#p.65
value = abs(-3)
print(value)                        # 절대값 반환

print(round(1.2345))                # 반올림 반환
print(round(1.9876))

# 최대값 구하기
print(max(10, 20))

# 최소값 구하기
print(min(10, 20, 30, 40, 50))

# 제곱 근 구하기
from math import *                  # 수학 함수 라이브러리 호출
print(sqrt(4.0))

x = 2.0
y = 3.0
print(sqrt(x**2 + y**2))

# p.67
route1 = 10
route2 = sqrt(3**2 + 4**2)
route3 = sqrt(3**2 + 4**2)
route4 = 8

result = (route1 + route4) / 20 + route2 / 10 + route3 / 30
print('주행하는데에 걸리는 시간은 ',result,'시간이다')
print('주행하는데에 걸리는 시간은 ' + str(int((result * 60) // 60)) + '시간 ' + str(int((result * 60) % 60)) + '분이다')

#p.74
price = 28000

#p.81
print('C:\some\name')               # 여기서 \n은 줄바꿈으로 잘못 해석된다
print(r'C:\some\name')              # 첫 따옴표 앞에 r을 추가하면 특수 문자의 의미를 없앨 수 있다.


