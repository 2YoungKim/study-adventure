# if-else 문 예시

signal_color = input('색을 영문으로 입력하세요: ')

if signal_color == 'blue':                                      # 파란색일 경우
    print('신호등은 파란색입니다. 건너세요.')
elif signal_color == 'red':
    print('신호등은 빨간색입니다. 기다리세요.')
else:                                                           # 파란색이 아닐 경
    print('잘못된 색입니다. 기다리세요.')


# while 문 예시

signal_color = ''                                               # 변수 선언 초기화
while signal_color != 'blue' and signal_color != 'red' :
    signal_color = input('색을 영문으로 입력하세요: ')

    if signal_color == 'blue' :
        print('신호등 파란색 건너라.')
    elif signal_color == 'red' :
        print('신호등 빨간색 건너면 죽는다.')
    else:
        print('잘못된 색 다시입력')

print(' 프로그램 종료한다. ')

