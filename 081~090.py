# 파이썬 딕셔너리

# 081 별 표현식
# 기본적으로 데이터 언패킹은 좌변의 변수와 우변 데이터 개수가 같아야 합니다. 하지만 star expression을
# 변수의 개수가 달라도 데이터 데이터 언패킹을 할 수 있습니다. 튜플에 저장된 데이터 중에서 앞에 있는 두 개의
# 데이터만 필요할 경우 나머지 데이터의 언패킹 코드를 작성할 필요가 없습니다.
# >> a, b, *c = (0, 1, 2, 3, 4, 5)
# >> a
# 0
# >> b
# 1
# >> c
# [2, 3, 4]
# 다음과 같이 10개의 값이 저장된 scores 리스트가 있을 때, start expression을 사용하여 좌측 8개의 값을 valid_score 변수에 바인딩하여라.
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
*valid_score, _, _ = scores
print(valid_score)

# 082
# 다음과 같이 10개의 값이 저장된 scores 리스트가 있을 때, start expression을 사용하여 우측 8개의 값을 valid_score 변수에 바인딩하여라.
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
_, _, *valid_score = scores
print(valid_score)

# 083
# 다음과 같이 10개의 값이 저장된 scores 리스트가 있을 때, start expression을 사용하여 가운데 있는 8개의 값을 valid_score 변수에 바인딩하여라.
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
_, *valid_score, _ = scores
print(valid_score)

# 084 비어있는 딕셔너리
# temp 이름의 비어있는 딕셔너리를 만들라.
temp = {}
print(type(temp), temp)

# 085
# 다음 아이스크림 이름과 희망 가격을 딕셔너리로 구성하라.
dict = {
    "메로나": 1000,
    "폴라포": 1200,
    "빵빠레": 1800
}
print(dict)

# 086
# 085 번의 딕셔너리에 아래 아이스크림 가격정보를 추가하라.
dict["죠스바"] = 1200
dict["월드콘"] = 1500
print(dict)

# 087 
# 다음 딕셔너리를 사용하여 메로나 가격을 출력하라.
print("메로나 가격: ",dict["메로나"])

# 088 
# 다음 딕셔너리에서 메로나의 가격을 1300으로 수정하라.
dict['메로나'] = 1300
print(dict)

# 089
# 다음 딕셔너리에서 메로나를 삭제하라
del dict["메로나"]
print(dict)

# 090
# 다음 코드에서 에러가 발생한 원인을 설명하라.
# >> icecream = {'폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
# >> icecream['누가바']
# Traceback (most recent call last):
#   File "<pyshell#69>", line 1, in <module>
#     icecream['누가바']
# KeyError: '누가바'
# 딕셔너리에 없는 키를 사용해서 인덱싱하면 에러가 발생합니다.
