# 231
# 아래 코드를 실행한 결과를 예상하라.

# def n_plus_1(n):
#     result = n + 1

# n_plus_1(3)
# print(result)

# 232
# 문자열 하나를 입력받아 인터넷 주소를 반환하는 make_url 함수를 정의하라.

def make_url(n):
    url = "www." + n + ".com"
    return url

def make_url1(n):
    return "www." + n + ".com"

# 233
# 문자열을 입력받아 각 문자들로 구성된 리스트로 반환하는 make_list 함수를 정의하라.

def make_list(string):
    my_list = []
    for 변수 in string:
        my_list.append(변수)
    return my_list

def make_list1(string):
    return list(string)    

# 234
# 숫자로 구성된 하나의 리스트를 입력받아, 짝수들을 추출하여 리스트로 반환하는
# pickup_even 함수를 구현하라.

def pickup_even(n):
    list1 = []
    for i in n:
        if list1 % 2 == 0:
            list1.append(i)
    return list1

# 235
# 콤마가 포함된 문자열 숫자를 입력받아 정수로 변환하는 convert_int 함수를 정의하라.

def convert_int(n):
    return int(n.replace(",",""))

# 236
# 아래 코드의 실행 결과를 예측하라.

def 함수(num):
    return num + 4

a = 함수(10) 
b = 함수(a) 
c = 함수(b) 
print(c)

# 237
# 아래 코드의 실행 결과를 예측하라.

def 함수1(num):
    return num + 4

c = 함수1(함수1(함수1(10)))
print(c)

# 238
# 아래 코드의 실행 결과를 예측하라.

def 함수2(num):
    return num + 4

def 함수3(num):
    return num * 10

a = 함수2(10)
c = 함수3(a)
print(c)

# 239
# 아래 코드의 실행 결과를 예측하라.
def 함수4(num):
    return num + 4

def 함수5(num):
    num = num + 2
    return 함수4(num)

c = 함수5(10)
print(c)

# 240
# 아래 코드의 실행 결과를 예측하라.
def 함수6(num):
    return num * 4

def 함수7(num):
    return 함수6(num + 2)

def 함수8(num):
    num = num + 10
    return 함수7(num)

c = 함수8(2)
print(c)