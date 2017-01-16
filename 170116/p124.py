def valToStr(x) :                       # 숫자로 한글로 변환하는 함수
    str_num = list()
    for i in range(0,len(str(x))) :     # 자리수를 정의. => length를 통해 몇 자리 수인지 알 수 있다.
        # str_num.insert(0, str(x)[i])
        str_num.append(str(x)[i])
        pass
    return numbering("".join(str_num))

def numbering(y) :                      # 숫자를 한글로 변환하기 위한 참조 함수
    num_list = ['영', '일', '이', '삼', '사', '오', '육', '칠', '팔', '구']
    tmp = list()
    for i in range(0,len(y)) :
        tmp.append(num_list[int(y[i])])
    #return "".join(tmp)
    return measure(tmp)

def measure(z) :                         # 십, 백, 천 등 자릿 수 에 대한 값 삽입
    z.reverse()
    for i in range(1, len(z) + 1):
        if ((i % 4) == 1):
            pass
        elif ((i % 4) == 2):
            if (z[i - 1] == '일') :
                z[i - 1] = '십'
            elif (z[i -1] == '영') :
                z[i - 1] = ''
            else :
                z[i - 1] = z[i - 1] + '십'
        elif ((i % 4) == 3):
            if (z[i - 1] == '일') :
                z[i - 1] = '백'
            elif (z[i -1] == '영') :
                z[i - 1] = ''
            else :
                z[i - 1] = z[i - 1] + '백'
        elif ((i % 4) == 0):
            if (z[i - 1] == '일') :
                z[i - 1] = '천'
            elif (z[i -1] == '영') :
                z[i - 1] = ''
            else :
                z[i - 1] = z[i - 1] + '천'
    if (len(z) > 12) :
        if (z[12] == '영') :
            z[12] = ''
        z.insert(12, '경 ')
    if (len(z) > 8) :
        if (z[8] == '영') :
            z[8] = ''
        z.insert(8, '억 ')
    if (len(z) > 4) :
        if (z[4] == '영') :
            z[4] = ''
        z.insert(4, '만 ')
    if (len(z) > 1 and z[0] == '영') :
        z[0] = ''
    if (z[10] == '' and z[11] == '' and z[12] == '' and z[13] == ''):
        z[9] = ''
    if (z[5] == '' and z[6] == '' and z[7] == '' and z[8] == ''):
        z[4] = ''
    z.reverse()
    return "".join(z)

# 숫자를 한글로 변환하는 코드 시작

chk = False

while chk == False :
    try :
        num = int(input("숫자를 입력하세요 : \n > "))
        if (num > 9999999999999999) :
            print("[ERROR!!] 값이 너무 큽니다.")
            chk = False
        else :
            chk = True
    except ValueError :
        print("[ERROR!!] 정수만 입력해주세요.")
        pass

print("입력 값 :", num, "[" + valToStr(num).strip() + "]")
print()
# 일 십 백 천
# 만 십만 백만 천만
# 억 십억 백억 천억
# 조 십조 백조 천조
# 경 십경 백경 천경