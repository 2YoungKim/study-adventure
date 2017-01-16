def my_func():
    userName = input('이름을 입력하세요 \n > ')
    print('Hello!', userName)

my_func()

def no_return():
    print('안녕하세요')
    return                                          #반환값 없음, 생략 가능

result = no_return()

print('함수 반환 값 출력 :',result)