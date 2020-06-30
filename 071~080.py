# 파이썬 튜플

# 071
# my_variable 이름의 비어있는 튜플을 만들라.
my_variable = ()
print(type(my_variable), my_variable)

# 072
# 2016년 11월 영화 예매 순위 기준 top3는 다음과 같다. 영화 제목을 movie_rank 이름의 튜플에 저장하라.(순위 정보는 저장하지 않는다.)
movie_rank = ("닥터 스트레인지", "스플릿", "럭키")
print(type(movie_rank), movie_rank)

# 073
# 숫자 1이 저장된 튜플을 생성하라.
my_tuple = (1, )
print(type(my_tuple), my_tuple)

# 074
# 다음 코드를 실행해보고 오류가 발생하는 원인을 설명하라.
# >> t = (1, 2, 3)
# >> t[0] = 'a'
# Traceback (most recent call last):
#   File "<pyshell#46>", line 1, in <module>
#     t[0] = 'a'
# TypeError: 'tuple' object does not support item assignment

# tuple은 원소의 값을 변경할 수 없다

# 075
# 아래와 값이 t에는 1, 2, 3, 4 데이터가 바인딩되어 있다. t가 바인딩하는 데이터 타입은 무엇인가?
t = 1, 2, 3, 4
print(type(t)) # 튜플, 원칙적으로 튜플은 괄호와 함께 데이터를 정의해야 하지만, 사용자 편의를 위해 괄호 없이도 동작합니다.

# 076
# 변수 t에는 아래와 같은 값이 저장되어 있다. 변수 t가 ('A', 'b', 'c') 튜플을 가리키도록 수정하라.
t = ('a', 'b', 'c')
# 튜플의 값은 변경할 수 없기 때문에, 리스트와 달리 아래 코드는 동작하지 않습니다.
# t[0] = 'A'
# 새로운 튜플을 만들고 t 라는 변수를 업데이트 해야 합니다. 기존의 튜플 ('a', 'b', 'c')은 자동으로 삭제됩니다.

# t = ('A', 'b', 'c')

# 077 
# 다음 튜플을 리스트로 변환하라.
interest = ('삼성전자', 'LG전자', 'SK Hynix')
print(list(interest))

# 078
# 다음 리스트를 튜플로 변경하라.
interest = ['삼성전자', 'LG전자', 'SK Hynix']
print(tuple(interest))

# 079 튜플 언팩킹
# 다음 코드의 실행 결과를 예상하라.
temp = ('apple', 'banana', 'cake')
a, b, c = temp
print(a, b, c)

# 080 range 함수
# 1부터 99까지의 정수 중 짝수만 저장된 튜플을 생성하라.
data = tuple(range(2, 100, 2))
print(data)
