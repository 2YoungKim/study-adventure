def main():
    n = int(input("정수를 입력하세요 \n > "))
    print(is_prime(n))

def is_prime(n):
    for i in range(2,n):
        if ( n % i == 0 ) :
            return False
    return True

main()