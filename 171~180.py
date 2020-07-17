# 171
# 아래와 같이 리스트의 데이터를 출력하라. 단, for 문과 range문을 사용하라.
price_list = [32100, 32150, 32000, 32500]

for i in range(4):
    print(price_list[i])

for i in range(len(price_list)):
    print(price_list[i])


# 172
# 아래와 같이 리스트의 데이터를 출력하라. 단, for 문과 range문을 사용하라.
price_list = [32100, 32150, 32000, 32500]
for i in range(len(price_list)):
    print(i, price_list[i])

# 173
# 아래와 같이 리스트의 데이터를 출력하라. 단, for 문과 range문을 사용하라.
price_list = [32100, 32150, 32000, 32500]

for i in range(len(price_list)):
    print(3 - i, price_list[i])

for i in range(len(price_list)):
    print(len(price_list) - i, price_list[i])

# 174
# 아래와 같이 리스트의 데이터를 출력하라. 단 for 문과 range문을 사용하라.
price_list = [32100, 32150, 32000, 32500]

for i in range(1,4):
    print(90 + 10 * i, price_list[i])

# 175
# my_list를 아래와 같이 출력하라.
my_list = ["가", "나", "다", "라"]

for i in [0, 1, 2]:
    print(my_list[i])

for i in [0, 1, 2]:
    print(my_list[i], my_list[i+1])

for i in range(len(my_list) - 1):
    print(my_list[i], my_list[i+1])

for i in range(1, len(my_list)):
    print(my_list[i-1] ,my_list[i])


print()
# 176
# 리스트를 아래와 같이 출력하라.
my_list = ["가", "나", "다", "라", "마"]

for i in range(2, len(my_list)):
    print(my_list[i-2],my_list[i-1],my_list[i])

print("---")
# 177
# 반복문과 range 함수를 사용해서 my_list를 아래와 같이 출력해라.
my_list = ["가", "나", "다", "라"]

for i in range(len(my_list) - 1, 0, -1):
    print(my_list[i], my_list[i-1])

# 178
# 리스트에는 네 개의 정수가 저장되어 있다. 각각의 데이터에 대해서 자신과 우측값과
# 의 차분값을 화면에 출력하라.
my_list = [100, 200, 400, 800]

for i in range(len(my_list) - 1):
    print(abs(my_list[i+1] - my_list[i]))

# 179
# 리스트에는 6일 간의 종가 데이터가 저장되어 있다. 종가 데이터의 3일 이동 평균을
# 계산하고 이를 화면에 출력하라.
my_list = [100, 200, 400, 800, 1000, 1300]

for i in range(1, len(my_list) - 1):
    print(abs(my_list[i-1] + my_list[i] + my_list[i+1]) / 3)

print()
# 180
# 리스트에 5일간의 저가, 고가 정보가 저장돼 있다. 고가와 저가의 차를 변동폭이라고
# 정의할 때, low, high 두 개의 리스트를 사용해서 5일간의 변동폭을 volatilty 리스트
# 에 저장하라.
low_prices  = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]
volatility = []

for i in range(len(low_prices)):
    volatility.append(high_prices[i] - low_prices[i])
print(volatility)