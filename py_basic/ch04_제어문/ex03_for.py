# 반복문
# for문
# 시퀀스 : 리스트, 튜플, 문자열, range()등
'''
    for 변수 in 시퀀스:
        실행문
'''

lst = ['one', 'two', 'three']
for i in lst:
    print(i)

a = [(1,2),(3,4),(5,6)]
for (first, last) in a:
    print(first + last)

marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number += 1
    if mark >= 60:
        print("%d번 학생은 합격입니다" % number)
    else:
        print("%d번 학생은 불합격입니다" % number)

# continue 문
marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number += 1
    if mark < 60:
        continue
    print("%d번 학생 축하합니다. 합격입니다" % number)

# range(시작, 끝) 함수
a = range(10) #갯수
print(a) # range(0, 10)

# 1부터 10까지 더하기
# range(1, 11): 1,2,3,...,10
sum = 0
# for i in [1,2,3,...,10]
for i in range(1, 11):
    sum += i # i값을 sum에 누적
print(sum)

# 합격 축하 문장 출력
# len() : 요소의 갯수
# range(5) : 0,1,2,3,4 -> range(0,5)
marks = [90, 25, 67, 45, 80]
for number in range(len(marks)):
    if(marks[number]) < 60:
        continue
    print(f"{number+1}번 학생 축하합니다. 합격입니다")

# print(값, end="\n")
# end의 기본값은 줄바꿈(\n)이다.
print("Hello", end="\n")
print("Hello")
print("Hello")
print("Hello", end=",")
print("Hello", end=" ")
print("Hello")

# 중첩 for 문
# 구구단
for i in range(2, 10): # i는 2단~9단
    for j in range(1, 10):
        print(i*j, end=" ")
    print('') # 줄 바꿈
'''
2 4 6 8 10 12 14 16 18
3 6 9 12 15 18 21 24 27
4 8 12 16 20 24 28 32 36
5 10 15 20 25 30 35 40 45
6 12 18 24 30 36 42 48 54
7 14 21 28 35 42 49 56 63
8 16 24 32 40 48 56 64 72
9 18 27 36 45 54 63 72 81
'''
for i in range(2, 10): # i는 2단~9단
    for j in range(1, 10):
        print(f"{i}*{j}={i*j:<2}", end="\t")  # <2는 자리 맞춤
    print()

from tabulate import tabulate

table = []
for i in range(2, 10):
    row = [f"{i}*{j}={i*j}" for j in range(1, 10)]
    table.append(row)

print(tabulate(table, tablefmt="grid"))


# 리스트의 각 항목에 3 곱하기
a = [1,2,3,4]
result = []
for num in a:
    result.append(num * 3)
print(result) # [3,6,9,12]

# 반복문 간소화
# list Comprehension(컴프리헨션)
# 시퀀스(반복가능객체): 리스트, 튜플, 문자열, range()
'''
    [표현식 for 항목 in 시퀀스 [if 조건문]]
'''
a = [1,2,3,4]
result = [num * 3 for num in a]
print(result) # [3, 6, 9, 12]

a = [1,2,3,4]
result = [num * 3 for num in a if num % 2 == 0]
print(result) # [6, 12]

print("===============")

# 구구단
result = [x*y for x in range(2,10)
          for y in range(1,10)]
print(result)

print("===============")

# break 문
for i in range(10):
    if i == 5:
        break
    print(i)

# for ~ else 문
for i in range(5):
    print(i)
else:
    print("for문이 정상 종료됩니다.")

# enumerate() : i를 알수있게 처리 (열거하다)
# -> 0부터 시작하는 인덱스 번호를 자동 생성
fruits = ["apple","banana", "orange"]
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")

fruits = ["apple","banana", "orange"]
for i, fruit in enumerate(fruits, 1): # 1부터 시작
    print(f"{i}: {fruit}")

# zip()
#
names = ['홍길동', '김철수', '이영자']
scores = [85, 92, 73]
for name, score in zip(names, scores):
    print(f"{name}: {score}점")