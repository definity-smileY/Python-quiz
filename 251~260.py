# 251 클래스, 객체, 인스턴스
# 클래스, 객체, 인스턴스에 대해 설명해봅시다.

""" class 클래스이름:
    인스터스명 = 클래스()
    객체.메서드() """

# 252 클래스 정의
# 비어있는 사람 (Human) 클래스를 "정의" 해보세요.
class Human():
    pass
# 253 인스턴스 생성
# 사람 (Human) 클래스의 인스턴스를 "생성" 하고 이를 areum 변수로 바인딩해보세요.
class Human():
    pass
areum = Human()

# 254 클래스 생성자 -1
# 사람 (Human) 클래스에 "응애응애"를 출력하는 생성자를 추가하세요.
class Human():
    print("응애응애")

areum = Human()

# 255 클래스 생성자 -2
# 사람 (Human) 클래스에 (이름, 나이, 성별)을 받는 생성자를 추가하세요.
class Human():
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex

areum = Human("아름", 25, "여자")
print(areum.name, areum.age, areum.sex)

# 256 인스터스 속성에 접근
# 255에서 생성한 인스턴스의 이름, 나이, 성별을 출력하세요. 인스턴스 변수에 접근하여 값을 출력하면 됩니다.
class Human():
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex

areum = Human("아름", 25, "여자")
print(areum.name, areum.age, areum.sex)

# 257 클래스 메소드 -1
# 사람 (Human) 클래스에서 이름, 나이, 성별을 출력하는 who() 메소드를 추가하세요.
class Human():
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
    
    def who(self):
        print("이름은 {}이고 나이는 {}이며 성별은 {}이야".format(self.name,self.age,self.sex))

areum = Human("홍길동", 25, "남자")
areum.who()

# 258 클래스 메소드 -2
# 사람 (Human) 클래스에 (이름, 나이, 성별)을 받는 setInfo 메소드를 추가하세요.
class Human():
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
    
    def who(self):
        print("이름은 {}이고 나이는 {}이며 성별은 {}이야".format(self.name,self.age,self.sex))

    def setInfo(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex

areum = Human("모름", 0, "모름")
areum.who()
areum.setInfo("아름", 25, "여자")
areum.who()

print()
# 259 클래스 소멸자
# 사람 (human) 클래스에 "나의 죽음을 알리지 말라"를 출력하는 소멸자를 추가하세요.
class Human():
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
    
    def __del__(self):
        print("나의 죽음을 적에게 알리지마라")
    
    def who(self):
        print("이름은 {}이고 나이는 {}이며 성별은 {}이야".format(self.name,self.age,self.sex))
    
    def setInfo(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex


areum = Human("아름", 25, "여자")
del(areum)

# 260 에러의 원인
# 아래와 같은 에러가 발생한 원인에 대해 설명하세요.
class OMG :
    def print() :
        print("Oh my god")


mystock = OMG()
mystock.print() # 에러
OMG.print() # 정답