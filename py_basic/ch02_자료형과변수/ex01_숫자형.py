# 주석
'''
문자열주석
'''
"""
문자열주석
1. 숫자: 정수(int), 실수(float)
2. 문자열(str)
3. 불(bool) : True, False(첫글자를 대문자로)
4. 시퀀스(sequence) : 리스트(list)
"""

# 정수형
# 사칙연산
# 복사 : shift+alt+방향키
# 같은 단어 선택 : ctrl+d : ddddd...
# 파이썬은 변수 선언 키워드가 없다.(동적변수)
a=123
print(a)
a = 0
print(a)
a = -123
print(a)
a = 3*9
print(a)
a = 3/2
print(a)

# 변수
a = 1
b = 2
print(a+b)

# 실수형
b = 1.2
print(b)
b = -3.14
print(b)

# e와 E 대소문자 구별 없음!
b = 4.24E5 # 4.24 * 10의 5승 -> 424000.0
print(b)
b = 4.24e-5 # 4.24 * 10의 -5승 -> 4.24e-05
print(b)
# 8진수 : 0o로 시작(알파벳 대소문자 구별 없음)
b = 0o177
print("8진수 : ", b)
# 16진수 : 0x로 시작
b = 0x8ff
c = 0xABC
print("16진수 : ", b, c)
print("=" * 80)

# 사칙 연산
a = 17
b = 3
print(a+b)
print(a-b)
print(a*b)
print(a/b)
# 산술 연산
print(a**b) # 거듭제곱 9 ** 3 = 9 * 9 * 9 = 729
print(a//b) # 몫
print(a%b)  # 나머지
print("=" * 80)

# 복합(대입+산술) 연산자
# +=, -=, *=, /=, %=, //=, **=
a = 1
a = a + 1
print("a =",a)
a+=1
print("a =",a)
a-=1
print("a =",a)
