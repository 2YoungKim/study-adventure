# 이름 장식 Nmae Mangling : __가 있는 것에 한하여 이름을 변경해 버리는
# 변형된 규칙 : _[클래스명]__[변수명]
# dir() : 클래스 내부에 들어있는 객체들을 확인하는 명령문
# 정보 은닉을 위해서 사용함

class BookReader:
    __country = 'Korea'
    __name = '철수'

result = dir(BookReader)
print(result)

num = 0
for internal_element in result:
    num += 1
    print(num, internal_element)

breader = BookReader
