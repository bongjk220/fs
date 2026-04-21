# 예외 예외 처리 기법
'''
try:
    실행코드
except [발생오류 [as 오류변수]]:
    실행코드
else:
    실행코드
finally:
    실행코드

try 블록 수행 중 오류가 발생하면 except 블록이 수행된다. 하지만 try 블록에서 오류가 발생하지 않는다면 except 블록은 수행되지 않는다.

finally 절은 try 문 수행 도중 예외 발생 여부에 상관없이 항상 수행된다. 보통 finally 절은 사용한 리소스를 close해야 할 때 많이 사용한다.
'''

try:
    f = open('foo.txt', 'w')
except FileNotFoundError as e:
    print(e)
finally:
    f.close() # 중간에 오류가 발생하더라도 무조건 실행된다.

try:
    print(4/0)
except ZeroDivisionError as e:
    print(e)
finally:
    print("finally 실행!")

print('-'*80)

# 여러 개의 오류 처리하기
try:
    a = [1,2]
    print(a[3]) # 여기서 오류발생하므로
    4/0 # 이곳은 에러 발생 안함
except (ZeroDivisionError, IndexError) as e:
    print(e)

print('-'*80)

# try_else.py
try:
    age=int(input('나이를 입력하세요: '))
except:
    print('입력이 정확하지 않습니다.')
else:
    try:
        print(4/0)
    except ZeroDivisionError as e:
        print(e)
    else:
        if age <= 18:
            print('미성년자는 출입금지입니다.')
        else:
            print('환영합니다.')
