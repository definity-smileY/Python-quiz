# 211
# 함수는 호출 결과를 예측하라.
def 함수(문자열):
    print(문자열)

함수("안녕")
함수("Hi")

# 212
# 함수의 호출 결과를 예측하라.
def 함수1(a, b):
    print(a + b)

함수1(3, 4) # 7
함수1(7, 8) # 15

# 213
# 아래와 같은 에러가 발생하는 원인을 설명하라.
# def 함수2(문자열):
#     print(문자열)

# 함수2()

# 함수에 정의와 다르게 함수를 호출하고 있다. 함수를 호출할 때 하나의 파라미터를
# 입력해야한다.

# 214
# 아래와 같은 에러가 발생하는 원인을 설명하라.
# def 함수(a, b):
#     print(a + b)

# 함수("안녕", 3)

# 정의된 함수는 같은 타입의 두 개의 값을 입력 받아 덧셈 연산을 적용하려는 의도로
# 설계되었습니다. 하지만 함수를 호출 할때 문자열과 숫자를 입력해서 문자열과 숫자는
# 더할 수 없다는 에러가 발생합니다.

# 215
# 하나의 문자를 입력받아 문자열 끝에 ":D" 스마일 문자열을 이어 붙여 출력하는
# print_with_smile 함수를 정의하라.

def print_with_smile(문자열):
    print(문자열, ":D")
    print(문자열 + ":D")

# 216
# 215에서 정의한 함수를 호출하라. 파라미터는 "안녕하세요"로 입력하라.

print_with_smile("안녕하세요")

# 217
# 현재 가격을 입력 받아 상한가(30%)를 출력하는 print_upper_price 함수를 정의하라.
def print_upper_price(가격):
    print(가격 * 1.3)

print_upper_price(5)

# 218
# 두 개의 숫자를 입력받아 두 수의 합을 출력하는 print_sum 함수를 정의하라.
def print_sum(a, b):
    print(a + b)

print_sum(10,20)

# 219
# 두 개의 숫자를 입력받아 합/차/곱/나눗셈을 출력하는 print_arithmetic_operation 함
# 수를 작성하라.
def print_arithmetic_operation(a, b):
    print("3 + 4 =",3 + 4)
    print("3 - 4 =",3 - 4)
    print("3 * 4 =",3 * 4)
    print("3 / 4 =",3 / 4) 

print_arithmetic_operation(3, 4)

# 220
# 세 개의 숫자를 입력받아 가장 큰 수를 출력하는 print_max 함수를 정의하라. 단 if 문
# 을 사용해서 수를 비교하라.
print()
def print_max(a, b, c):
    num = 0
    if a > num:
        num = a
    if b > num:
        num = b
    if c > num:
        num = c

    print(num)

print_max(10, 20, 30)

