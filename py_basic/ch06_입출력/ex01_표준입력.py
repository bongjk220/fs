# 표준 입력
# input()
age = input("숫자를 입력하세요: ")
print(type(age)) # <class 'str'>
print(age)
# 문자와 숫자를 더하므로 오류
# nxtAge = age + 1 # TypeError: can only concatenate str (not "int") to str 
print("30년후 나이는 %d입니다." % (int(age)+30))

# 실수로 변환
# float(); 문자열을 실수로 변환
# 1m = 100cm
height = float(input("키를 입력하세요(cm): "))
height /= 100
#print("미터로 환산하면 %0.2f(m)입니다." % (int(height)/100))
print("미터로 환산하면 %0.2f(m)입니다." % height)

# 