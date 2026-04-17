# 표준 출력
'''
    print(값, 값, ...., sep=' ', end='\n')
        sep(seperate)는 구분자로 기본값은 공백
        end는 끝낮추기 기본값은 \n
'''

# print()
print("Life is too short")
print("Life","is","too","short")
# 모두 문자열이면 +는 연결
# 모두 숫자이면 덧셈
print("Life "+"is "+"too "+"short ")
print("Life","is","too","short", sep=":")
'''
Life is too short
Life is too short
Life:is:too:short
'''

# end의 기본값 \n
print("Life", end="\n")
print("is")
print("too")
print("short")

print("Life", end=" ")
print("is", end=" ")
print("too", end=" ")
print("short")
print("2026", "04", "16", sep="-")
'''
Life
is
too
short
Life is too short
2026-04-16
'''

# 반복문으로 예
for i in range(5):
    print(i)

for i in range(5):
    print(i, end=" ")
'''
0
1
2
3
4
0 1 2 3 4
'''