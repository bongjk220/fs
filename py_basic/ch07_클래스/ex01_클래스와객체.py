# calculator2.py
result1 = 0
result2 = 0

print("=================함수만 사용==================")

def add1(num):  # 계산기1
    global result1
    result1 += num
    return result1

def add2(num):  # 계산기2
    global result2
    result2 += num
    return result2

print(add1(3))
print(add1(4))
print(add2(3))
print(add2(7))

print("=================클래스 이용==================")

# calculator2.py



class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result

    def sub(self, num):
        self.result -= num
        return self.result

# 객체 : cal1, cal2
# 클래스(class)란 똑같은 무언가를 계속 만들어 낼 수 있는 설계 도면(과자 틀)이고, 객체(object)란 클래스로 만든 피조물(과자 틀로 찍어 낸 과자)을 뜻한다.
# 객체마다 고유한 성격을 가진다는 것
# 클래스로 만든 객체를 '인스턴스'라고도 한다. 
# a = Cookie()
# a는 객체이다.
# a는 Cookie 클래스로 만든 인스턴스이다.
cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))

print(cal1.sub(3))
print(cal1.sub(4))
print(cal2.sub(3))
print(cal2.sub(7))

print("===================================")

class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second