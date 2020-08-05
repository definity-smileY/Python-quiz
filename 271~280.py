# 271 Account 클래스
# 은행에 가서 계좌를 개설하면 은행이름, 예금주, 계좌번호, 잔액이 설정됩니다. Account 클래스를 생성한 후 생성자를 구현해보세요. 생성자에서는 예금주와 초기 잔액만 입력 받습니다. 은행이름은 SC은행으로 계좌번호는 3자리-2자리-6자리 형태로 랜덤하게 생성됩니다.
import random
class Account():
    
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
        self.bank = "SC제일은행"

        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)
        self.account_number = num1 + '-' + num2 + "-" + num3

a = Account("SC제일은행",None)
print("은행이름 : "+a.name,"계좌번호 :"+a.account_number)

print()
# 272 클래스 변수
# 클래스 변수를 사용해서 Account 클래스로부터 생성된 계좌 객체의 개수를 저장하세요.
import random
class Account():
    account_count = 0
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
        self.bank = "SC제일은행"

        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)
        self.account_number = num1 + '-' + num2 + "-" + num3

        Account.account_count += 1
a = Account("SC제일은행",None)
print("은행이름 : "+a.name,"계좌번호 :"+a.account_number)

kim = Account("김민수", "100")
print(Account.account_count)
lee = Account("이민수", "100")
print(Account.account_count)

print()
# 273 클래스 변수 출력
# Account 클래스로부터 생성된 계좌의 개수를 출력하는 get_account_num() 메서드를 추가하세요.
import random
class Account():
    account_count = 0
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
        self.bank = "SC제일은행"

        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)
        self.account_number = num1 + '-' + num2 + "-" + num3

        Account.account_count += 1

    def get_account_num(self):
        print(Account.account_count)


kim = Account("김민수", 100)
lee = Account("이민수", 100)
kim.get_account_num()


# 274 입금 메서드
# Account 클래스를 입금을 위한 deposit 메서드를 추가하세요. 입금은 최소 1원 이상만 가능합니다.
import random
class Account():
    account_count = 0
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
        self.bank = "SC제일은행"

        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)
        self.account_number = num1 + '-' + num2 + "-" + num3

        Account.account_count += 1

    def get_account_num(self):
        print(Account.account_count)

    def deposit(self, amount):
        if amount >= 1:
            self.balance += amount

# 275 출금 메서드
# Account 클래스에 출금을 위한 withdraw 메서드를 추가하세요. 출금은 계좌의 잔고 이상으로 출금할 수는 없습니다.
import random

class Account:
    # class variable
    account_count = 0

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.bank = "SC은행"

        # 3-2-6
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3)      # 1 -> '1' -> '001'
        num2 = str(num2).zfill(2)      # 1 -> '1' -> '01'
        num3 = str(num3).zfill(6)      # 1 -> '1' -> '0000001'
        self.account_number = num1 + '-' + num2 + '-' + num3  # 001-01-000001
        Account.account_count +=1

    @classmethod
    def get_account_num(cls):
        print(cls.account_count)     # Account.account_count

    def deposit(self, amount):
        if amount >= 1:
            self.balance += amount
    
    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
    
k = Account("kim", 0)
k.deposit(100)
k.withdraw(90)
print(k.balance)

# 276 정보 출력 메서드
# Account 인스턴스에 저장된 정보를 출력하는 display_info() 메서드를 추가하세요. 잔고는 세자리마다 쉼표를 출력하세요.
import random

class Account:
    # class variable
    account_count = 0

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.bank = "SC은행"

        # 3-2-6
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3)      # 1 -> '1' -> '001'
        num2 = str(num2).zfill(2)      # 1 -> '1' -> '01'
        num3 = str(num3).zfill(6)      # 1 -> '1' -> '0000001'
        self.account_number = num1 + '-' + num2 + '-' + num3  # 001-01-000001
        Account.account_count += 1

    @classmethod
    def get_account_num(cls):
        print(cls.account_count)     # Account.account_count

    def deposit(self, amount):
        if amount >= 1:
            self.balance += amount
    
    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount

    def display_info(self):
        print("은행이름:", self.bank)
        print("예금주", self.name)
        print("계좌번호", self.account_number)
        print("잔고","{:,}".format(self.balance)+"원")

p = Account("파이썬", 10000)
p.display_info()
        
# 277 이자 지급하기
# 입금 횟수가 5회가 될 때 잔고를 기준으로 1%의 이자가 잔고에 추가되도록 코드를 변경해보세요.
class Account:
    account_count = 0

    def __init__(self, name, balance):
        self.deposit_count = 0
        self.name = name
        self.balance = balance
        self.bank = "SC은행"

        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)

        self.account_number = num1 + "-" + num2 + "-" + num3

        Account.account_count += 1

    def get_account_num(cls):
        print(cls.account_count)

    def deposit(self, amount):
        if amount >= 1:
            self.balance += amount

            self.deposit_count += 1
            if self.deposit_count % 5 == 0:
                self.balance = (self.balance * 1.01)

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount

    def display_info(self):
        print("은행이름: ", self.bank)
        print("예금주: ", self.name)
        print("계좌번호: ", self.account_number)
        print("잔고: ","{:,}".format(self.balance)+"원")

p = Account("파이썬", 10000)
p.deposit(10000)
p.deposit(10000)
p.deposit(10000)
p.deposit(5000)
p.deposit(5000)
print(p.balance)

# 278 여러 객체 생성
# Account 클래스로부터 3개 이상 인스턴스를 생성하고 생성된 인스턴스를 리스트에 저장해보세요.
class Account:
    account_count = 0

    def __init__(self, name, balance):
        self.deposit_count = 0
        self.name = name
        self.balance = balance
        self.bank = "SC은행"

        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)

        self.account_number = num1 + "-" + num2 + "-" + num3

        Account.account_count += 1

    def get_account_num(cls):
        print(cls.account_count)

    def deposit(self, amount):
        if amount >= 1:
            self.balance += amount

            self.deposit_count += 1
            if self.deposit_count % 5 == 0:
                self.balance = (self.balance * 1.01)

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount

    def display_info(self):
        print("은행이름: ", self.bank)
        print("예금주: ", self.name)
        print("계좌번호: ", self.account_number)
        print("잔고: ","{:,}".format(self.balance)+"원")
    
data = []
h = Account("홍길도", 1000)
l = Account('이이', 1000)
k = Account("킬킬", 10000)

data.append(h)
data.append(l)
data.append(k)
print(data)

# 279 객체 순회
# 반복문을 통해 리스트에 있는 객체를 순회하면서 잔고가 100만원 이상인 고객의 정보만 출력하세요.
class Account:
    account_count = 0

    def __init__(self, name, balance):
        self.deposit_count = 0
        self.name = name
        self.balance = balance
        self.bank = "SC은행"

        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)

        self.account_number = num1 + "-" + num2 + "-" + num3

        Account.account_count += 1

    def get_account_num(cls):
        print(cls.account_count)

    def deposit(self, amount):
        if amount >= 1:
            self.balance += amount

            self.deposit_count += 1
            if self.deposit_count % 5 == 0:
                self.balance = (self.balance * 1.01)

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount

    def display_info(self):
        print("은행이름: ", self.bank)
        print("예금주: ", self.name)
        print("계좌번호: ", self.account_number)
        print("잔고: ","{:,}".format(self.balance)+"원")

data = []
h = Account("홍길도", 1000)
l = Account('이이', 1000000)
k = Account("킬킬", 10000)

data.append(h)
data.append(l)
data.append(k)

for i in data:
    if i.balance >= 1000000:
        i.display_info()
print("==========")
# 280 입출금 내역
# 입금과 출금 내역이 기록되도록 코드를 업데이트 하세요. 입금 내역과 출금 내역을 출력하는 deposit_history와 withdraw_history 메서드를 추가하세요.
class Account:
    account_count = 0

    def __init__(self, name, balance):
        self.deposit_count = 0
        self.deposit_log = []
        self.withdraw_log = []
        self.name = name
        self.balance = balance
        self.bank = "SC은행"

        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)

        self.account_number = num1 + "-" + num2 + "-" + num3

        Account.account_count += 1

    def get_account_num(cls):
        print(cls.account_count)

    def deposit(self, amount):
        if amount >= 1:
            self.balance += amount

            self.deposit_count += 1
            if self.deposit_count % 5 == 0:
                self.balance = (self.balance * 1.01)

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount

    def display_info(self):
        print("은행이름: ", self.bank)
        print("예금주: ", self.name)
        print("계좌번호: ", self.account_number)
        print("잔고: ","{:,}".format(self.balance)+"원")
    
    def withdraw_history(self):
        for amount in self.withdraw_log:
            print(amount)
    
    def deposit_history(self):
        for amount in self.deposit_log:
            print(amount)

k = Account("Kim", 1000)
k.deposit(100)
k.deposit(200)
k.deposit_history()
k.display_info()
k.withdraw(100)
k.withdraw(200)
k.withdraw_history()
k.display_info()