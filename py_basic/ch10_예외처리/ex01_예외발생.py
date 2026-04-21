# 예외?
# 프로그램에서 자주 발생하는 오류
# f = open("나없는파일", 'r')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# FileNotFoundError: [Errno 2] No such file or directory: '나없는파일'
try:
    f = open("나없는파일", 'r')
except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")
# 파일을 찾을 수 없습니다.

#print(4/0)
#ZeroDivisionError: division by zero
# try ~ except
try:
    print(4/0)
except ZeroDivisionError:
    print("0으로 나눌 수  없습니다.")

a = [1,2,3]
# print(a[3])
# IndexError: list index out of range
try:
    print(a[3])
except IndexError:
    print("인덱싱 할 수 없습니다.")

# try ~ except ~ else
try:
    f = open("나없는파일", 'r')
except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")
else:
    print(f.read())
    f.close