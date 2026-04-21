# 상속 
# 상속(Inheritance)이란 '물려받다'라는 뜻으로, '재산을 상속받다'라고 할 때의 상속과 같은 의미이다. 클래스에도 이 개념을 적용할 수 있다. 
# 클래스를 상속하기 위해서는 다음처럼 클래스 이름 뒤 괄호 안에 상속할 클래스 이름을 넣어주면 된다.
'''
    class MoreFourCal(FourCal):
        pass
'''

class FourCal:
    # 생성자
    def __init__(self, first, second):
        self.first = first
        self.second = second

    # 메서드(method)
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result

class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result

a = MoreFourCal(4,2)
print(a.add()) # 6
print(a.mul()) # 8
print(a.sub()) # 2
print(a.div()) # 2.0
print(a.pow()) # 16

# 내장함수
print('-'*80)
print(pow(2,3)) # 2의 3제곱
print(2 ** 3) # 2의 3제곱
print(pow(10, -1)) # 10의 -1제곱
print(10 ** -1) # 10의 -1제곱
print(pow(2, 10, 7)) # 2의 10제곱을 7로 나머지
print(2 ** 10 % 7) # 2의 10제곱을 7로 나머지

class Mother:
    def skill(self):
        print('요리 실력')

class Father:
    def hobby(self):
        print('축구 시청')

# 다중상속이 가능하다
class Child(Mother, Father):
    def study(self):
        print('코딩 공부')

c = Child()
c.skill()
c.hobby()
c.study()