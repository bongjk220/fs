# 생성자(constructor)란?
# 객체가 생성될 때 자동으로 호출되는 메서드
# 파이썬 메서드명으로 __init__를 사용하면 이 메서드는 생성자가 된다.
# 객체가 생성될때 자동으로 생성
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
    
a = FourCal(4, 2)
print(a.first)
print(a.second)

print(a.add())
print(a.mul())
print(a.sub())
print(a.div())