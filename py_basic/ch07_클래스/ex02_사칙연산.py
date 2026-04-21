# 사칙연산 클래스

# 1. 클래스를 어떻게 만들지 구상하기
'''
1. 클래스명 : FourCal
2. 매서드명 :
    setData() : 두 개의 수를 지정
    add() : 두 수의 합
    sub() : 두 수의 차
    mul() : 두 수의 곱
    div() : 두 수의 나머지

    a = FourCal()
    a.setdata(4, 2)
    a.add() -> 6
    a.sub() -> 2
    a.mul() -> 8
    a.div() -> 2.0
'''

# 2. 클래스 구조 만들기
# 클래스 안에 구현된 함수는 다른 말로 메서드(method)라고 부른다.
class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second
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


# 3. 객체 만들기
a = FourCal()
print(type(a)) # <class '__main__.FourCal'>
# 객체 a가 FourCal 클래스로 만든 객체임을 알수있다.

# '클래스명.매서드' 형태로 호출할 때는 객체 a를 첫번째 매개변수 self에 꼭 전달해야 한다.
a.setdata(4, 2)
print(a.first) # 4
print(a.second) # 2

# 객체에 생성되는 객체변수를 '인스턴스 변수' 또는 '속성' 이라고 부른다.
b = FourCal()
b.setdata(3, 7)
print(b.first) # 3
print(b.second) # 7

print(a.add()) # 6
print(b.add()) # 10

print(a.mul()) # 8
print(b.mul()) # 21

print(a.sub()) # 2
print(b.sub()) # -4

print(a.div()) # 2.0
print(b.div()) # 0.42857142857142855

print('-'*80)

class Calculator2:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result

    def sub(self, num):
        self.result -= num
        return self.result

    def mul(self, num):
        self.result *= num
        return self.result

    def div(self, num):
        self.result /= num
        return self.result

    def mod(self, num):
        self.result %= num
        return self.result

    def pow(self, num):
        self.result **= num
        return self.result

    def floor(self, num):
        self.result //= num
        return self.result

    def clear(self):
        self.result = 0
        return self.result

    def get_result(self):
        return self.result

    def set_result(self, num):
        self.result = num
        return self.result

    def __str__(self):
        return str(self.result)

    def __repr__(self):
        return str(self.result)

    def __bool__(self):
        return bool(self.result)

    def __int__(self):
        return int(self.result)

    def __float__(self):
        return float(self.result)

    def __complex__(self):
        return complex(self.result)

    def __oct__(self):
        return oct(self.result)

    def __hex__(self):
        return hex(self.result)

    def __bin__(self):
        return bin(self.result)

    def __abs__(self):
        return abs(self.result)

    def __round__(self):
        return round(self.result)

    def __len__(self):
        return len(str(self.result))

    def __getitem__(self, index):
        return str(self.result)[index]

    def __setitem__(self, index, value):
        str(self.result)[index] = value
        return str(self.result)

    def __delitem__(self, index):
        del str(self.result)[index]
        return str(self.result)

    def __reversed__(self):
        return reversed(str(self.result))

    def __contains__(self, item):
        return item in str(self.result)

    def __iter__(self):
        return iter(str(self.result))

    def __next__(self):
        return next(str(self.result))

    def __reversed__(self):
        return reversed(str(self.result))

    def __reversed__(self):
        return reversed(str(self.result))

