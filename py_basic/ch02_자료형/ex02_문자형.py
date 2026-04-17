# 문자열을 만드는 방법
print("Hello")
print('Hello')
print('''Life is too shoot,You need python''')
print("""Life is too shoot,You need python""")

# 문자열에 작은 따옴표 포함하기
food = "Python's favorite food is perl"
print(food)

# 문자열에 큰 따옴표 포함하기
food = '"Python\'s favorite food" is perl'
print(food)

# 줄바꿈(\n)
food = '"Python\'s favorite food"\n is perl'
print(food)
print('''Life is too shoot,
      You need python''')
print("""
      Life is too shoot,
      You need python
      """)

# 문자열 연산
head = "Python"
tail = "3.11.2"
# 문자열 연결(문자열 끼리만)
print(head + tail)

# 문자열 반복
print(head * 2)

# 문자열 길이(Length): len()
a="Life is too shoot,You need python"
print(len(a))

# 문자열 인덱싱과 슬라이싱
# 인덱싱 : ~을 가르킨다.
print(a[3])
print(a[0])
print(a[-0])
print(a[12])
print(a[-1])
print(a[-2])
print(a[-5])
# 슬라이싱 : 어디부터 어디까지
print(a[0:4]) # 0~3 -> 4이전, 4는 포함x
print(a[0:5]) # 0~4
print(a[0:2]) # 0~1
print(a[5:7]) # 5,6
print(a[12:17]) # 12,13,14,15,16

print("-----------------------------")
print(a[19:])   # 19부터 끝까지
print(a[:17])   # 처음부터 17이전까지
print(a[:])     # 처음부터 끝까지
print(a[19:-7]) # 19~끝에서 7번째까지

# 슬라이싱으로 문자열 나누기
a = "20260406Sunny"
date = a[:8]
year = a[:4]
day = a[4:8]
weather = a[8:]
print(year + "년")
print(day)
print(weather)

# 문자열 대체(i -> y)
a = "Pithon"
print(a)
# a[1] = 'y' # 문자열은 변경 불가능한 자료형이므로 에러 발생
print(a[:1]+'y'+a[2:]) # 문자열 슬라이싱으로 변경
a = a.replace("i", "y")
print(a)    

# 문자열 포맷팅
'''
%d 숫자(digit
%s 문자열(string)
'''
print("I eat %d apples." % 3)
print("I eat %s apples." % "three")

number = 3
print("I eat %d apples." % number)

# 2개 이상의 값 넣기
number = 10
day = "three"
print("I eat %d apples. so I was sick for %s days." % (number, day))

# %% -> 리터럴(literal), 특수문자 %fh 지정
# 포맷 코드와 숫자 함께 사용하기
print("Error is %d%%." % 98) # %% -> % 문자 자체
print("Error is %2.1f%%." % 3.5) # %% -> % 문자 자체

# 포맷 코드와 숫자 함께 사용하기
print("1234567890")
print("%10s" % "hi") # 전체 10자리 중에서 오른쪽 정렬
print("%-10sJane" % "hi") # 전체 10자리 중에서 왼쪽 정렬
print("%10.4f" % 3.141592) # 전체 10자리 중에서 소수점 4자리까지 표현

### v2.6+ 이후 format() 함수 사용
# 문자열 포맷팅 함수
print("I eat {0} apples.".format(3))
print("I eat {0} apples.".format("five"))
number = 3
print("I eat {0} apples.".format(number))
number = 10
day = "three"
print("I eat {0} apples. so I was sick for {1} days.".format(day, number))
print("I eat {1} apples. so I was sick for {0} days.".format(number, day))
# 이름으로 넣기
print("I eat {number} apples. so I was sick for {day} days.".format(number=number, day=day))

print("-----------------------------")

# 정렬 
print("{0:<10}".format("hi")) # 왼쪽 정렬
print("{0:>10}".format("hi")) # 오른쪽 정렬
print("{0:^10}".format("hi")) # 가운데 정렬 (캐럿)

# 포맷 코드와 숫자 함께 사용하기
print("I eat {0:5d} apples.".format(3)) # 전체 5자리 중에서 오른쪽 정렬
print("I eat {0:5d} apples.".format(10)) # 전체 5자리 중에서 오른쪽 정렬
print("I eat {0:5d} apples.".format(100)) # 전체 5자리 중에서 오른쪽 정렬
print("I eat {0:5d} apples.".format(1000)) # 전체 5자리 중에서 오른쪽 정렬
print("I eat {0:5d} apples.".format(10000)) # 전체 5자리 중에서 오른쪽 정렬
print("I eat {0:5d} apples.".format(100000)) # 전체 5자리 중에서 오른쪽 정렬
print("I eat {0:5.2f} apples.".format(3.141592)) # 전체 5자리 중에서 소수점 2자리까지 표현
print("I eat {0:5.2f} apples.".format(10.141592)) # 전체 5자리 중에서 소수점 2자리까지 표현
print("I eat {0:5.2f} apples.".format(100.141592)) # 전체 5자리 중에서 소수점 2자리까지 표현
print("I eat {0:5.2f} apples.".format(1000.141592)) # 전체 5자리 중에서 소수점 2자리까지 표현
print("I eat {0:5.2f} apples.".format(10000.141592)) # 전체 5자리 중에서 소수점 2자리까지 표현
print("I eat {0:5.2f} apples.".format(100000.141592)) # 전체 5자리 중에서 소수점 2자리까지 표현

# 특정 문자로 공백 채우기
print("{0:=^10}".format("hi")) # 가운데 정렬, 공백 대신 =로 채우기
print("{0:!<10}".format("hi")) # 왼쪽 정렬, 공백 대신 !로 채우기
print("{0:!>10}".format("hi")) # 오른쪽 정렬, 공백 대신 !로 채우기

# 소수점 표현하기
y = 3.141592
print("{0:0.4f}".format(y)) # 소수점 4자리까지 표현, 전체 자릿수는 자동으로 계산
print("{0:10.4f}".format(y)) # 소수점 2자리까지 표현, 전체 자릿수는 자동으로 계산

# 특수문자 { } 안에 그대로 표시하기
print("{{ and }}".format()) # { and } -> {,} 문자 자체 표현

### v3.6+ f문자열 포맷팅
name = "홍길동"
age = 30
print("나의 이름은 {name}. 나이는 {age} 입니다.".format(name=name, age=age)) # 예전방식
print(f"나의 이름은 {name}. 나이는 {age} 입니다.") # f-string 사용, 변수명 그대로 사용
print(f"나의 내년이면 {age+1}살이 된다.") 

### 딕셔너리
d = {'name': '홍길동', 'age': 30}
print(d)
print("나의 이름은 {0[name]}. 나이는 {0[age]} 입니다.".format(d)) # 딕셔너리의 키를 이용하여 값 출력
print(f"나의 이름은 {d['name']}. 나이는 {d['age']} 입니다.") # f-string 사용, 딕셔너리의 키를 이용하여 값 출력

# 정렬
print(f"{'hi':<10}") # 왼쪽 정렬
print(f"{'hi':>10}") # 오른쪽 정렬
print(f"{'hi':^10}") # 가운데 정렬 (캐럿)

# 공백 채우기
print(f"{'hi':=^10}") # 가운데 정렬, 공백 대신 =로 채우기
print(f"{'hi':=<10}") # 왼쪽 정렬, 공백 대신 !로 채우기
print(f"{'hi':=>10}") # 오른쪽 정렬, 공백 대신 !로 채우기

# 소수점
y = 3.141592
print(f"{y:0.4f}") # 소수점 4자리까지 표현, 전체 자릿수는 자동으로 계산
print(f"{y:10.4f}") # 소수점 4자리까지 표현, 전체 자릿수는 자동으로 계산

#{} 문자 그대로 표현하기
print(f"{{ and }}") # { and } -> {,} 문자 자체 표현

# 천단위 표시
number = 1500000
print(f"난 {number:,}원이 필요해!") # 천단위 구분자 , 사용