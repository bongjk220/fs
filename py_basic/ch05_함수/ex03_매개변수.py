# 가변 매개변수

# 매개변수 앞에 *를 붙이면 가변 매개변수가 된다.
# 가변 매개변수는 함수에 전달된 인수들을 튜플로 만들어준다.
# *args -> (1,2,3)
def add_many(*args):
    result = 0
    for i in args:
        result += i
    return result

print(add_many(1,2,3)) # 6
print(add_many(1,2,3,4,5)) # 15

# 선택한 매개변수와 가변 매개변수를 함께 사용할 수 있다.
# 가변 매개변수는 마지막에 사용해야한다.
def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result += i
    elif choice == "mul":
        result = 1
        for i in args:
            result *= i
    return result

print(add_mul("add", 1,2,3,4,5)) # 15
print(add_mul("mul", 1,2,3,4,5)) # 120

# 키워드(keyword) 매개변수
# 함수 호출시 key=value 형태로 전달하는 매개변수를 받을 때
# 입력받은 키워드 매개변수들을 딕셔너리 형태로 출력
def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(a=1) # {'a': 1}
print_kwargs(name='foo', age=3) # {'name': 'foo', 'age': 3}
print_kwargs(name='홍길동', age=25, city='서울', job='개발자') # {'name': '홍길동', 'age': 25, 'city': '서울', 'job': ': '개발자'}

# **info -> {'이름':'김철수', '나이':30, '직업':'개발자'}
def create_profile(**info):
    print("=== 프로필 정보 ===")
    for key, value in info.items():
        print(f"{key}: {value}")

create_profile(이름='김철수', 나이=30, 직업='개발자')
'''
=== 프로필 정보 ===
이름: 김철수
나이: 30
직업: 개발자
'''

#매개변수의 순서는 일반->가변->키워드
def mixed_fuction(name, *args, **kwargs):
    print(f"이름 : {name}")
    print(f"추가 인수들: {args}")
    print(f"키워드 인수들: {kwargs}")

mixed_fuction('홍길동', 1,2,3, age=25, city='서울')
'''
이름 : 홍길동
추가 인수들: (1, 2, 3)
키워드 인수들: {'age': 25, 'city': '서울'}  
'''

# 매개변수 기본값
def final_para(a, b=10):
    print(f"일반 : {a}, 기본값: {b}")

final_para(1)
final_para(1, 2)
'''
일반 : 1, 기본값: 10
일반 : 1, 기본값: 2
'''

print("-------------------")

# 순서 : 일반->기본값->가변->키워드전용->키워드가변
def final_para(a, b=10, *args, k=20, **kwargs):
    print(f"일반 : {a}, 기본값: {b}")
    print(f"가변 : {args}")
    print(f"키워드 전용 : {k}")
    print(f"키워드 가변 : {kwargs}")

final_para(1,2,3,4,5, k=100, name="홍길동", age=30)
'''
일반 : 1, 기본값: 2
가변 : (3, 4, 5)
키워드 전용 : 100
키워드 가변 : {'name': '홍길동', 'age': 30}   
'''

# 
def say_myself(name, age, man=True):
    print("나의 이름은 %s 입니다." % name)
    print("나이는 %d살입니다." % age)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")

say_myself("홍길동", 27)
# 값을 주면 man의 기본값 무시된다.
say_myself("이오리", 30, False)
say_myself("이기자", 15, True)
'''
나의 이름은 홍길동 입니다.
나이는 27살입니다.
남자입니다.
나의 이름은 이오리 입니다.
나이는 30살입니다.
여자입니다.
나의 이름은 이기자 입니다.
나이는 15살입니다.
남자입니다.
'''


    