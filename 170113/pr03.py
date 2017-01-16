# break문 예시


signals='blue','yellow','red'

# for x in range(len(signals)):
#     print(x, signals[x],'루프시작!!')
#     if signals[x] == 'yellow':
#         break
#     print(x, signals[x],'루프종료!')
#
# print('프로그램 종료')

for x in range(len(signals)):
    print(x, signals[x], '루프시작!!')
    if signals[x] == 'yellow':
        continue
    print(x, signals[x], '루프종료!')

print('프로그램종료')

for x in range(len(signals)):
    print(x, signals[x], '루프시작!!')
    if signals[x] == 'yellow':
        pass
    print(x, signals[x], '루프종료!')

print('프로그램종료')
