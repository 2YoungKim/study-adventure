# http://www.pythonchallenge.com/pc/def/map.html
# g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
'''
def thisistheproblem(code):                         # 함수 정의 - 문자를 입력받으면 a = 0 부터 z = 25 까지 26가지의 숫자로 변환 해주는 함수
    return ord(code.lower()) - 97                   # 소문자 a의 10진수 ascii code 값 = 97 ord() 함수는 문자열을 ascii code 10진수로 표현해주는 함수

def hereistheanswer(code):                          # 함수 정의 - thisistheproblem() 함수를 역으로 풀이함. 숫자를 알파벳으로 표현
    return chr(code+97)                             # 숫자를 ascii code 값으로 변환

problem = input('input: ')                          # 문제의 값을 입력받음
answer = int(input('key : '))                       # 2 를 입력

result = ""                                         # 변수 초기화

for i in problem:                                   # problem 문자열의 length 값 만큼 반복(loop)
    if(95<ord(i) and ord(i)<123):                   # 알파벳일 때만 가능하게 해라.
        index = thisistheproblem(i)
        result += hereistheanswer((index+answer)%26)# hereistheanswer()함수를 쓰면 result에 chr(code+97)이 되기 때문에 들어가면안됨.
                                                    # result += (index+answer) 가 맞는 표현.
    else:
        result += i                                 # pass 가 들어가야함. i 를 더하면 안됨. -> 띄어쓰기가 있는 스페이스바의 경우
                                                    # ascii code 32 로 받는데 - 96을 했으니 예외가 발생함. 스페이스바는 그대로 두어야한다.
print(int(result))                                  # print(hereistheanswer(result)) 가 되어야한다. result를 대신 int형으로 받아야한다.
                                                    # 문자열로 제대로 받아주는 구문이없다. + 추가로 적어주어야할 것.
'''
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
# OPTION 1
'''
def thisistheproblem(code):
    return ord(code.lower()) - 96

def hereistheanswer(code):
    return chr(code+96)

problem = input('[ 암호를 입력하세요 ]\n'
                ' > ')
answer = input('[ 덧셈 규칙을 입력하세요 ]\n'
               ' + ')
#
result = []

for i in problem:
    if(95<ord(i) and ord(i)<123):
        index = thisistheproblem(i)
        result.append(hereistheanswer(index+int(answer)))
    else:
        pass
print ("".join(result))
'''
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
# OPTION 2
def encodeToChr(ascii) :
    if ( 91 < ascii < 96 ) or ( 122 < ascii ) :
        return chr(ascii - 26)
    else :
        return chr(ascii)

def request() :
    problem = input('[ 암호를 입력하세요 ]\n'
                    ' > ')
    logic = int(input('[ 덧셈 규칙을 입력하세요 ]\n'
                   ' + '))
    return problem, logic

def processing( pw, lgc ) :
    result = []
    for i in pw :
        ascii = ord(i)
        if ((64 < ascii) and (ascii < 91)) or ((96 < ascii) and (ascii < 123)) :
            result.append(encodeToChr(ascii + lgc))
        else :
            result.append(i)
    return result

password, logic = request()
print("".join(processing(password, logic)))

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
# if  (( 64 < ascii ) & ( ascii < 91 )) | (( 96 < ascii ) & ( ascii < 123 )) :