# type
# type(object)는 입력값의 자료형이 무엇인지 알려 주는 함수
print(type(123)) # <class 'int'>
print(type("abc")) # <class 'str'>
print(type([1,2,3])) # <class 'list'>
print(type((1,2,3))) # <class 'tuple'>
print(type({1,2,3})) # <class 'set'>
print(type({1:'a',2:'b',3:'c'})) # <class 'set'>
print(type(True)) # <class 'bool'>
print(type(range(10))) # <class 'range'>
print(type(open("test", 'w'))) # <class '_io.TextIOWarpper'>

# isinstance
# isinstance(object, class)는
# 첫 번째 인수로 객체,
# 두 번째 인수로 클래스를 받는다.
# 입력받은 객체가 해당 클래스의 인스턴스인지 판단하여
# 참이면 True, 거짓이면 False를 반환
class Person: pass
a = Person()
isinstance(a, Person)
print(isinstance(a, Person)) # True
b = 3
isinstance(b, Person)
print(isinstance(b, Person)) # False

# id
# id(object)는 객체를 입력받아 객체의 고유 주솟값(레퍼런스)을 반환
# id 값은 실행 환경과 시점에 따라 달라질 수 있다.
a = 3
print(id(3)) # 140719791494328
print(id(a)) # 140719791494328
b = a
print(id(b)) # 140719791494328
print(id(4)) # 140719791494360

# dir
# 객체가 지닌 변수나 함수를 보여 주는 함수
print(dir([1,2,3]))
print(dir({'1':'a'}))

