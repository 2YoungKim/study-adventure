# 클래스 변수 (인스턴스 간 공유 됨)
print('초기화를 하지 않은 클래스 변수로 선언 할 경우 \n')

class Dog:
    tricks = [] # 클래스 변수 선언

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)

dog1 = Dog('마음이')
dog2 = Dog('진돌이')

dog1.add_trick('구르기')
dog2.add_trick('두 발로 서기')
dog2.add_trick('죽은척 하기')

print(dog1.name, ':', dog1.tricks)
print(dog2.name, ':', dog2.tricks)

print('')
print('초기화를 한 인스턴스 변수로 선언 할 경우 \n')

class Cat:
    def __init__(self, name):
        self.name = name
        self.tricks = [ ]               # 인스턴스 변수 선언

    def add_trick(self, trick):
        self.tricks.append(trick)   # 인스턴스 변수에 값 추가

cat1 = Cat('하늘이')
cat2 = Cat('야옹이')

cat1.add_trick('구르기')
cat2.add_trick('두 발로 서기')
cat2.add_trick('죽은척 하기')

print(cat1.name, ':', cat1.tricks)
print(cat2.name, ':', cat2.tricks)