class BookReader:
    country = 'Republic Of Korea'

    def __init__(self, name):
        self.name = name

    def read_book(self):
        print(self.name, 'is reading Book!!')

# 객체 인스턴스화
reader1 = BookReader('David')
reader2 = BookReader('John')

# 클래스 변수 country 확인
print('reader1.country:', reader1.country)
print('reader2.country:', reader2.country,'\n')

reader1.read_book()
reader2.read_book()