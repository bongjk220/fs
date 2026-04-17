# 함수의 유형
# 
def add(a, b):
    result = a + b
    return result

a = add(3,4)
print(a)

# 매가변수가 없다.
def say():
    return "Hi"

a = say()
print(a) #Hi

# 매개변수 있고, 반환값이 없는 경우
def add(a, b):
    print("%d, %d의 합은 %d입니다."% (a, b, a+b))


a = add(3,4) # 3, 4의 합은 7입니다.
print(a) # None

# 4. 매개변수 없고, 반환값도 없는 경우
def say():
    print("Hi")

say()

# 5. 매개변수의 이름을 명시적으로 지정하여 함수를 호출할 수 있다.
# 매개변수를 지정하여 호출
# 매개변수의 순서와 이름이 달라도 된다.
def sub(a, b):
    return a - b

result = sub(7, 3)
print(result) # 4

result = sub(a=7, b=3)
print(result) # 4 

result = sub(b=3, a=7)
print(result) # 4    