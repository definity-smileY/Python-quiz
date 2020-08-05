# 281 클래스 정의
# 다음 코드가 동작하도록 차 클래스를 정의하세요.
class car():
    def __init__(self,바퀴,가격):
        self.바퀴 = 바퀴
        self.가격 = 가격
    
car = car(2, 1000)
print(car.바퀴)
print(car.가격)

# 282 클래스 상속
# 차 클래스를 상속받는 자전차 클래스를 정의하세요.
class car():
    def __init__(self,바퀴,가격):
        self.바퀴 = 바퀴
        self.가격 = 가격

class 자전차(car):
    pass

# 283 클래스 상속
# 다음 코드가 동작하도록 자전차 클래스를 정의하세요. 단 자전차 클래스는 차 클래스를 상속받습니다.
class car():
    def __init__(self,바퀴,가격):
        self.바퀴 = 바퀴
        self.가격 = 가격

class 자전차(car):
    def __init__(self,바퀴,가격):
        self.바퀴 = 바퀴
        self.가격 = 가격


bicycle = 자전차(2, 100)
print(bicycle.가격)

# 284 클래스 상속
# 다음 코드가 동작하도록 자전차 클래스를 정의하세요. 단 자전차 클래스는 차 클래스를 상속받습니다.
class car():
    def __init__(self,바퀴,가격):
        self.바퀴 = 바퀴
        self.가격 = 가격

class 자전차(car):
    def __init__(self,바퀴,가격,구동계):
        super().__init__(바퀴,가격)
        self.구동계 = 구동계

bicycle = 자전차(2, 100, "시마노")
print(bicycle.구동계)

# 285 클래스 상속
# 다음 코드가 동작하도록 차 클래스를 상속받는 자동차 클래스를 정의하세요.
class car():
    def __init__(self, 바퀴, 가격):
        self.바퀴 = 바퀴
        self.가격 = 가격
    
class 자동차(car):
    def __init__(self, 바퀴, 가격):
        super().__init__(바퀴, 가격)
    
    def 정보(self):
        print("바퀴수 : ", self.바퀴)
        print("가격 : ", self.가격)

car = 자동차(4, 1000)
car.정보()

# 286 부코 클래스 생성자 호출
# 다음 코드가 동작하도록 자전차 클래스를 수정하세요.
class car():
    def __init__(self, 바퀴, 가격):
        self.바퀴 = 바퀴
        self.가격 = 가격
    
    def 정보(self):
        print("바퀴수 :", self.바퀴)
        print("가격 : ", self.가격)
class 자동차(car):
    def __init__(self, 바퀴, 가격):
        super().__init__(바퀴, 가격)

class 자전차(car):
    def __init__(self, 바퀴, 가격, 구동계):
        super().__init__(바퀴, 가격)
        self.구동계 = 구동계

bicycle = 자전차(2, 100, "시마노")
bicycle.정보()

# 287 부모 클래스 메서드 호출
# 자전차의 정보() 메서드로 구동계 정보까지 출력하도록 수정해보세요.
class car():
    def __init__(self, 바퀴, 가격):
        self.바퀴 = 바퀴
        self.가격 = 가격

    def 정보(self):
        print("바퀴수 : ", self.바퀴)
        print("가격 : ", self.가격)

class 자동차(car):
    def __init__(self, 바퀴, 가격):
        super().__init__(바퀴, 가격)

class 자전차(car):
    def __init__(self, 바퀴, 가격, 구동계):
        super().__init__(바퀴, 가격)
        self.구동계 = 구동계    
    
    def 정보(self):
        super().정보()
        print("구동계 : ", self.구동계)
        
bicycle = 자전차(2, 10, "시마노")
bicycle.정보()

# 288 메서드 오버라이딩
# 다음 코드의 실행 결과를 예상해보세요.
class 부모:
    def 호출(self):
        print("부모호출")

class 자식(부모):
    def 호출(self):
        print("자식호출")
    
나 = 자식()
나.호출()

# 289 부모클래스 생성자 호출
# 다음 코드의 실행 결과를 예상해보세요.
class 부모:
    def __init__(self):
        print("부모호출")

class 자식(부모):
    def __init__(self):
        print("자식생성")
        super().__init__()

나 = 자식()       