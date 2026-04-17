# 변수 선언과 사용
# 변수 선언
# a, b, c를 변수라고 한다.
a = 1
b = "python"
c = [1,2,3]

# 변수 명명 규칙
'''
1. 영문자, 숫자, 언더스코어(_)만 사용!
2. 숫자로 시작x
3. 예약어X
4. 대소문자 구분
'''

# 올바른 예시
name = "홍길동"
age = 25
user_name = "hong"
userName = "hong" # 대소문자 구분
_private = "비공개"
count1 = 10

# 잘못된 예시
# 1name = "홍길동" # 숫자로 시작x
# user-name = "hong" # 하이픈(-)은 사용할 수 없음
# if = "MyClass" # 예약어X
# user name = "hong" # 공백X

# 변수명(권장 사항)
'''
1. 의미있는 명확한 이름으로 작성
2. 너무 짧거나 너무 긴 이름은 피한다.
3. snake_case 권장(파이썬)
4. 공백X
5. 변수명은 소문자로 작성하는 것이 관례
6. 여러 단어로 구성된 변수명은 언더스코어(_)로 구분하는 것이 관례
'''

# 예시
student_name = "홍길동" # 의미있는 명확한 이름
total_score = 95 # 의미있는 명확한 이름
user_age = 20 # 의미있는 명확한 이름

# 피해야할 예시
a = 100 # 의미없는 이름
studentNameFormKorea = "홍길동" # 너무 긴 이름

# 변수란? 객체를 가리키는 것
# 객체란? 자료형의 데이터(값)와 같은 것
# [1,2,3] 값을 가지는 리스트 객체가 메모리에 생성되고
# 변수가 기리키는 객체의 주소 값을 반환한다.
a = [1,2,3]
b = a # a가 가리키는 객체의 주소 값을 b도 가리키게 된다.
print(a) # [1, 2, 3]
print(id(a)) # 2336536432960 -> 객체의 주소 값
print(id(b)) # 2336536432960 -> 객체의 주소 값
print(type(a)) # <class 'list'>

# 튜플로 a, b에 값을 대입할 수 있다
a, b = ('python', 'java')
print(a) # python
print(b) # java

# 튜플은 괄호 생략 가능
a, b = 'python', 'java'
print(a) # python
print(b) # java

# 리스트
[a, b]  = ['python', 'java']
print(a) # python
print(b) # java

# 여러개의 변수에 같은 값을 대입할 수 있다.
a = b = 'python'
print(a) # python
print(b) # python

# 두 변수의 값 교환
a = 3
b = 5
a, b = b, a
print(a) # 5
print(b) # 3



# 변수 삭제
a = 10
print(a) # 10
del a # a라는 변수를 삭제한다.
# print(a) # error -> a라는 변수가 존재하지 않음

# 변수의 범위
def my_function():
    x = 10 # 지역 변수
    print(x)
my_function() # 10
# print(x) # error -> x라는 변수가 존재하지 않음
