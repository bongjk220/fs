# 제어문
'''
1. 조건문 : if, if-else, if-elif-else
            switch-case문이 없다. -> 3.10+ match~case문으로 대체한다.
2. 반복문 : for, while
3. 기타 : break, continue, pass
'''

# if문
# 예) 돈이있으면 택시를 타고, 없으면 걸어간다.
money = 2000
card = True

# 조건문 다음에 콜론(:)
# 들여쓰기
if money > 3000 or card:
    print("택시를 타고 간다.")
else:
    print("걸어간다.")

# in, not in
print(1 in [1,2,3]) # True
print(4 in [1,2,3]) # False
print(1 not in [1,2,3]) # False
print(4 not in [1,2,3]) # True
print('a' in ['a', 'b', 'c']) # True
print('j' in 'python') # False
print('p' in 'python') # True

pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    print("택시를 타고 간다.")
else:
    print("걸어간다.")

print("-----------------------------")

# pass : 조건문에서 아무 일도 하지 않게 설정(임시조치)
pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    pass
else:
    print("걸어간다.")

print("-----------------------------")


pocket = ['paper', 'cellphone']
card  = True
if 'money' in pocket:
    print("택시를 타고 간다.")
else:
    if card:
        print("카드로 결제하여 택시를 타고 간다.")
    else:
        print("걸어간다.")

print("-----------------------------")

# if-elif-else문
pocket = ['paper', 'cellphone']
card  = True

if 'money' in pocket:
    print("택시를 타고 간다.")
elif card:
    print("카드로 결제하여 택시를 타고 간다.")
else:
    print("걸어간다.")

if 'money' in pocket: print("택시를 타고 간다.")
elif card: print("카드로 결제하여 택시를 타고 간다.")
else: print("걸어간다.")

print("-----------------------------")

# match-case문(파이썬 3.10+)
# 성적 예시
grade = "B"

if grade == "A":
    print("탁월한 성적입니다.")
elif grade == "B":
    print("우수한 성적입니다.")
elif grade == "C":
    print("보통 성적입니다.")
elif grade == "D":
    print("미흡한 성적입니다.")
else:
    print("노력 필요!")

grade = "B"
match grade:
    case "A":
        print("탁월한 성적입니다.")
    case "B":
        print("우수한 성적입니다.")
    case "C":
        print("보통 성적입니다.")
    case "D":
        print("미흡한 성적입니다.")
    case _:
        print("노력 필요!")

# 합겹/불합격
grade = "B"
match grade:
    case "A" | "B" | "C":
        print("합격입니다.")
    case "D" | "F":
        print("불합격입니다.")
    case _:
        print("노력 필요!")

# 연쇄 비교 연산자
x = 5
print(1 < x)
#print(1 < x)
print(x < 10)

# x는 1보다 크고 10보다 작다.
print(1 < x and x < 10) # True
print(1 < x < 10) # True

# 조건부 표현식 : 둘 중 하나
'''
    변수 = 참일때의 값 if 조건문 else 거짓일때의 값
'''
score = 85
result = "합격" if score >= 60 else result = "불합격"
print(result) # 합격

# 조건부 표현식으로 작성