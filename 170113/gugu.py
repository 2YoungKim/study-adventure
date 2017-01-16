# 구구단을 외자
checkNum = False                                                                        # 사용자로부터 받은 입력값이 정수가 맞는지 확인하는 변수, 초기값은 False로 세팅

while checkNum == False :                                                               # 사용자가 입력한 값이 정수가 아니라면,
    try:                                                                                #
        userNum = int(input("몇 단을 출력할까요? \n > "))                               # 입력 값 요구
        checkNum = True                                                                 # 입력 값이 int형으로 형변환이 가능한 경우

    except ValueError:
        print("정수만 입력해주세요.")
        pass

for i in range(1, 10) :
    print("[" + str(userNum) + "단]", userNum, "X", i , "=", userNum * i)