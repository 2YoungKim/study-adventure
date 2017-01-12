# 리스트 항목 제거하기 : remove ()함수

pockets = [ 1, 2, 3, 4 ]
print(pockets)

pockets.remove(1)               # 특정 값 제거
print(pockets)

# 리스트 항목 삽입하기 : insert() 함수
pockets.insert(1,3)             # 두번 째 색인1)에 3 삽입
print(pockets)

# 리스트 항목 추출하기 : pop() 함수
pockets.pop(3)                  # 네번째 값 반환 후 제거
print(pockets)

pockets = [ 1, 2, 3, 4 ]

# 리스트형 복사하기
pockets_copy = pockets[:]       # 신규 변수 생성 및 기존 리스트 대
pockets_copy.append(1)          # 신규 변수에 1 추가

print('pockets : ', pockets)
print('pockets_copy : ', pockets_copy)
print(id(pockets))
print(id(pockets_copy))


a = [ 1, 2, 3 ]
b = [ 4, 5, 6 ]
print('a = ', a)
print('b = ', b)
print('id(a) = ', id(a))
print('id(b) = ', id(b))

# 리스트형 데이터 확장
a.extend(b)
print('a = ', a)
print('id(a) = ', id(a))

#리스트 삭제를 위한 del() 함수
a = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
print('a = ', a)
del a[0]
print('del a[0] -> a = ', a)

a = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
print('a = ', a)
del a[1:3]
print('del a[1:3] -> a = ', a)

a = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
print('a = ', a)
del a[:]
print('del a[:] -> a = ', a)

# Error
#a = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
#print('a = ', a)
#del a
#print('del a[] -> a = ', a)

# 3X3 2차원 행렬을 중첩 리스트로 선언
nest = [ [ 1, 2, 3 ], [ 4, 5, 6 ], [ 7, 8, 9 ] ]

print('nest 크기 : ', len(nest))
print(nest)
print(nest[0])
print(nest[0][0])

word = '파이썬 문자열 색인'
print('word => ', word)
print('word[:3] => ', word[:3])
print('word[:4] => ', word[4:])
print('word[-2:] => ', word[-2:])

# 튜플 자료형
print ( ' ' )
print ( ' 튜플 자료형 ')
print ( ' ' )

movie = '슈퍼맨II', 1980, '배트맨', 1989
print ( movie )
print ( movie[1] )
print ( movie[-2:] )

# 튜플값 변경 시도 (형오류발생)
#movie[1] = 1982

movie_list = list(movie)        # 튜플 -> 리스트형 변환
print(type(movie_list))         # 데이터형 확인
print(movie_list )              # 데이터값 확인 (대괄호 기호 확인)
print(tuple(movie_list))        # 리스트 -> 튜플형 변환(소괄호 기호 확인)

print ( ' ' )
print ( ' [ 세트형 자료 ] ')
print ( ' ' )

# 세트형 생성
lang = { 'Java', 'Java', 'Python', 'C++', 'Python' }
print( lang )

# 세트형값 확인 (중복 제거 확인)
print( 'Java' in lang )         # 항목 존재 유무 확인
print( 'javascript' in lang )


print ( ' ' )
print ( ' [ 세트형 집합연산자 ] ')
print ( ' ' )

a = set('abracadabra')
b = set('alacazam' )
print( 'a = ', a )
print( 'b = ', b )
print( '차집합, a - b = ', a-b )
print( '합집합, a | b = ', a|b )
print( '교집합, a & b = ', a&b )
print( '여집합, a ^ b = ', a^b )
a = set('abracadabra')
b = set('alacazam' )
print( 'a = ', a )
print( 'b = ', b )
print( '차집합, a - b = ', a-b )
print( '합집합, a | b = ', a|b )
print( '교집합, a & b = ', a&b )
print( '여집합, a ^ b = ', a^b )

print ( ' ' )
print ( ' [ 사전형 자료 ] ')
print ( ' ' )

balls = { 'red' : 4, 'blue' : 3, 'green' : 5 }
print( balls )                  # 사전형 값 확인
print( type(balls) )            # 데이터 형 확인
print( len(balls) )             # 사전형 길이 확인

# 검은 공 항목 추가
balls['black'] = 1
print(balls)

# 값 변경
balls['black'] = 3
print(balls)

# 녹색 공 항목 제거
del balls['green']
print( balls )

# 사전 키 추출 후 리스트형
print( list(balls.keys()) )     # 사전 키 추출 후 리스트 형으로 전환
print( sorted(balls.keys()) )   # 사전 키 추출 후 오름차순 정렬
print( list(balls.values()) )   # 사전 값 추출 후 리스트 형으로 변환

print( 'blue' in balls )        # 키존재 유무 확인
print( 'white' not in balls )   # 키누락 유무 확인

# dict 표기 1
balls1 = { 'red' : 4, 'blue' : 3, 'green' : 5 }
print(" 방법 1 : ", balls1)

# 리스트 안의 항목이 키와 값의 쌍으로 이루어진 튜플인 경우
balls2 = dict( [('brown',3 ), ('gray', 7)] )
print(" 방법 2 : ", balls2)

# 키가 단순한 문자열인 경우 dict 함수의 인자값 형태로 진행
balls3 = dict( brown = 4, gray = 8 )
print(" 방법 3 : ", balls3)
