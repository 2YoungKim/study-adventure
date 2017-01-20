# 상속
# 객체지향의 꽃

# 부모 클래스 Human
class Human:
    country = 'Korea'

    def __init__(self, name):
        self.name = name

    def eat_meal(self):
        print(self.name, 'is eating meal!!')

# Human의 Child-Class인 Book Reader 클래스
class BookReader(Human):
    def read_book(self):
        print(self.name, 'is reading Book!!')

# Human의 Child-Class인 Drum Player 클래스
class DrumPlayer(Human):
    def play_drum(self):
        print(self.name, 'is playing Drum!!')

br = BookReader('ChangYoung')
br.eat_meal()
br.read_book()

dp = DrumPlayer('JuneYoung')
dp.eat_meal()
dp.play_drum()

print('\n') # 타입확인
print('br.__class__:', br.__class__)                     # br 인스턴스의 타입 확인
print('BookReader.__class__:', BookReader.__class__)    # BookReader 클래스의 타입 확인
print('BookReader.__bases__:', BookReader.__bases__)    # BookReader 클래스의 부모 클래스 확인
print('Human.__class__:', Human.__class__)              # Type of Human Class
print('Human.__bases__:', Human.__bases__)
# 파이썬은 C나 자바와 달리 다중 상속이 가능하다. 하지만 먼저 상속된 부모 값이 우선순위를 갖는다. 즉, __bases__로 호출해보면 먼저 상속된 값이 호출된다.
