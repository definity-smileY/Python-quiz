# 파이썬 분기문

# 101
# 파이썬에서 True 혹은 False를 갖는 데이터 타입은 무엇인가?

print(type(bool())) # bool타입

# 102
# 아래 코드의 출력 결과를 예상하라
print(3 == 5) # False뜰것

# 103
# 아래 코드의 출력 결과를 예상하라
print(3 < 5) # True뜰것

# 104
# 아래 코드의 결과를 예상하라.
x = 4
print(1 < x < 5)
# True 뜰것

# 105
# 아래 코드의 결과를  예상하라
print((3 == 3) and (4 != 3))
# True 뜰것

# 106
# 아래 코드에서 에러가 발생하는 원인에 대해 설명하라.
# print(3 => 4) >=이 맞다
print(3 >= 4) # False

# 107
# 아래 코드의 출력 결과를 예상하라.
if 4 < 3:
    print("Hello world") # False

# 108
# 아래 코드의 출력 결과를 예상하라
if 4 < 3:
    print("Hello world.")
else:
    print("Hi, there.")
# Hi, there.가 뜰것

# 109
# 아래 코드의 출력 결과를 예상하라
if True:
    print("1")
    print("2")
else:
    print("3")
print("4") # 124 만뜬다

# 110
# 아래 코드의 출력 결과를 예상하라
if True:
    if False:
        print("1")
        print("2")
    else:
        print("3")
else:
    print("4")
print("5") # 3 5 만 뜬다

