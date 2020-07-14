# 파이썬 분기문

# 121
# 사용자로부터 문자 한 개를 입력 받고, 소문자일 경우 대문자로, 대문자 일 경우, 소문
# 자로 변경해서 출력하라.
# q1 = input("스펠링 입력 : ")
# if q1.islower():
#     print(q1.upper())
# else:
#     print(q1.lower())

# 122
# 점수 구간에 해당하는 학점이 아래와 같이 정의되어 있다.
# score = int(input("score : "))

# if score >= 81:
#     print(score ,"is A")
# elif score >= 61:
#     print(score ,"is B")
# elif score >= 41:
#     print(score ,"is C")
# elif score >= 21:
#     print(score ,"is D")
# else:
#     print(score ,"is E")

# 123
# 사용자로부터 달러, 엔, 유로, 또는 위안 금액을 입력받은 후 이를 원으로 변환하는 프
# 로그램을 작성하라. 각 통화별 환율은 다음과 같다. 사용자는 100달러, 1000엔, 13유로,
# 100위안과 같이 금액과 통화명 사이에 공백을 넣어 입력한다고 가정한다.

# money = {
#     "달러": 1167,
#     "엔" : 1.096,
#     "유로" : 1268,
#     "위안" : 171,
# }
# user = input("금액 : ")

# k, v = user.split()

# print(float(k) * money[v], "원")

# 124
# 사용자로부터 세 개의 숫자를 입력 받은 후 가장 큰 숫자를 출력하라.

# a = input("input number1: ")
# b = input("input number2: ")
# c = input("input number3: ")
# a = int(a)
# b = int(b)
# c = int(c)

# if a > b and a > c:
#     print(a)
# elif b > a and b > c:
#     print(b)
# else:
#     print(c)

# 125
# 휴대폰 번호 앞자리에 따라 통신사는 아래와 같이 구분된다. 사용자로부터 휴대전화
# 번호를 입력 받고, 통신사를 출력하는 프로그램을 작성하라.

# number = input("휴대전화 번호입력 : ")
# num = number.split("-")[0]
# if num == "011":
#     com = "SKT"
# elif num == "016":
#     com = "KT"
# elif num == "019":
#     com = "LGU"
# else:
#     com = "알수없음"

# print(f"당신은 {com} 입니다.")

# 126
# 우편번호는 5자리로 구성되는데, 앞의 세자리는 구를 나타낸다. 예를 들어, 강북구의
# 경우 010, 011, 012 세 자리로 시작한다.

# 우편번호 = input("우편번호 : ")
# 우편번호 = 우편번호[:3]
# if 우편번호 in ["010","011","012"]:
#     print("강북구")
# elif 우편번호 in ["014","015","016"]:
#     print("도봉구")
# else:
#     print("노원구")

# 127
# 주민등록번호 뒷 자리 7자리 중 첫째 자리는 성별을 나타내는데, 1,3은 남자 2,4는
# 여자를 의미한다. 사용자로부터 13자리의 주민등록번호를 입력 받은 후 성별 (남자, 여자)를
# 출력하는 프로그램을 작성하라.
# 주민번호 = input("주민등록번호 : ")
# 주민번호 = 주민번호.split("-")[1]
# if 주민번호[0] == "1" or 주민번호 == "3":
#     print("남자")
# else:
#     print("여자")

# 128
# 주민등록번호의 뒷 자리 7자리 중 두번째와 세번째는 지역코드를 의미한다. 주민 등
# 록 번호를 입력 받은 후 출생지가 서울인지 아닌지 판단하는 코드를 작성하라
# 주민등록번호 = input("주민등록번호 : ")
# 주민등록번호 = 주민등록번호.split("-")[1]
# if 0 <= int(주민등록번호[1:3]) <= 8:
#     print("서울입니다.")
# else:
#     print("서울이 아닙니다.")

# 129
# 주민등록번호는 13자리로 구성되는데 마지막 자리수는 주민등록번호의 유효성을 체크하는데 사용된다.
# 먼저 앞에서부터 12자리의 숫자에 2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5를 차례로 곱한 뒤 그 값을 전부 더한다. 
# 연산 결과 값을 11로 나누면 나머지가 나오는데 11에서 나머지를 뺀 값이 주민등록번호의 마지막 번호가 된다.
# num = input("주민등록번호 : ")
# 계산1 = int(num[0]) * 2 + int(num[1]) * 3 + int(num[2]) * 4 + int(num[3]) * 5 + int(num[4]) * 6 + \
#     int(num[5]) * 7 + int(num[7]) * 8 + int(num[8]) * 9 + int(num[9]) * 2 + int(num[10]) * 3 + \
#         int(num[11]) * 4 + int(num[12]) * 5

# 계산2 = 11 - (계산1 % 11)
# 계산3 = str(계산2)

# if num[-1] == 계산3[-1]:
#     print("유효한 주민등록번호입니다.")
# else:
#     print("유효하지 않은 주민등록번호입니다.")

# 130
# 아래 코드는 비트코인의 가격 정보를 딕셔너리로 가져오는 코드이다.
import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']
# btc 딕셔너리 안에는 시가, 종가, 최고가, 최저가 등이 저장되어 있다. 최고가와 최저
# 가의 차이를 변동폭으로 정의할 때 (시가 + 변동폭)이 최고가 보다 높을 경우 "상승장",
# 그렇지 않은 경우 "하락장" 문자열을 출력하라.
변동폭 = float(btc['max_price']) - float(btc['min_price'])
시가 = float(btc['opening_price'])
최고가 = float(btc['max_price'])

if (시가+변동폭) > 최고가:
    print("상승장")
else:
    print("하락장")