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

# 매서드 재정의(overriding)
a = FourCal(4, 0)
print(a.add())
print(a.mul())
print(a.sub())
#print(a.div()) # ZeroDivisionError: division by zero

class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second

a = SafeFourCal(4, 0)
print(a.add())
print(a.mul())
print(a.sub())
print(a.div()) # ZeroDivisionError: division by zero

b = SafeFourCal(4, 2)
print(b.div()) # ZeroDivisionError: division by zero