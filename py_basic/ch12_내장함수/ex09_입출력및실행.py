# input
# input([prompt])는 사용자 입력을 받는 함수이다.
# 입력 인수로 문자열을 전달하면 그 문자열은 프롬프트가 된다.
# a = input()
# print(a)
b = input("Enter: ")
print(b)

with open("test.txt", "w", encoding="utf-8") as f:
    f.write("안녕하세요!")

# open
# open(filename, [mode])은 '파일 이름'과 '읽기 방법'을 입력받아
# 파일 객체를 반환
# 읽기 방법(mode)을 생략하면
# 기본값인 읽기 모드(r)로 파일 객체를 만들어 반환
# w: 쓰기 모드로 파일 열기
# r: 읽기 모드로 파일 열기
# a: 추가 모드로 파일 열기
# b: 바이너리 모드로 파일 열기
f = open("test.txt", "r", encoding="utf-8")
data = f.read()
print(data)
f.close

# eval
# eval(expression)은 문자열로 구성된 표현식을 입력으로 받아
# 해당 문자열을 실행한 결괏값을 반환
# eval은 입력 문자열을 실제로 실행하므로,
# 신뢰할 수 없는 외부 입력에는 사용하면 안 된다.
print(eval('1+2')) # 3
print(type(eval('1+2'))) # <class 'int'>
print(eval("'hi' + 'a'")) # hia
print(eval('divmod(4, 3)')) # (1, 1)