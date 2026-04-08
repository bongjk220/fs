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
# 인덱싱이란 ~을 가르킨다.
print(a[3])
print(a[0])
print(a[-0])
print(a[12])
print(a[-1])
print(a[-2])
print(a[-5])
# 슬라이싱이란 어디부터 어디까지
print(a[0:4]) # 0~3 -> 4이전, 4는 포함x
print(a[0:5]) # 0~4
print(a[0:2])
print(a[5:7])
print(a[12:17])