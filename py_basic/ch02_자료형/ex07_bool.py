# boolean(불)
a = True
b = False
print(a)
print(b)

# type() : 자료형을 알려주는 함수
print(type(a))
print(type(b))

# 비교 연산자의 결과는 Ture 또는 False입니다.
print(5 > 3)  # True
print(5 < 3)  # False
print(5 == 5)  # True
print(5 != 5)  # False
print(5 >= 3)  # True
print(5 <= 3)  # False

print("-----------------------------")

# bool() : 자료형을 불로 변환하는 함수
print(bool(1))  # 1은 True
print(bool(-1))  # -1은 True
print(bool("Hello"))  # 빈 문자열이 아니면 True
print(bool([1, 2, 3]))  # 빈 리스트가 아니면 True
print(bool(3.14))  # 0이 아닌 실수는 True

print(bool(""))  # 빈 문자열은 False
print(bool([]))  # 빈 리스트는 False
print(bool(()))  # 빈 튜플은 False
print(bool({}))  # 빈 딕셔너리는 False
print(bool(0))  # 0은 False
print(bool(None))  # None은 False

print("-----------------------------")

# 논리 연산의 결과도 True 또는 False입니다.
print(True and True)  # True
print(True and False)  # False
print(False and True)  # False
print(False and False)  # False
print(True or True)  # True
print(True or False)  # True
print(False or True)  # True
print(False or False)  # False
print(not True)  # False
print(not False)  # True


# 논리/비교 활용 예시
x = 5
y = 10
print(x > 0 and y > 0)  # True
print(x > 10 or y > 5)  # True
print(not (x > y))  # True