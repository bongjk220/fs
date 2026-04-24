# 부모클래스
class Bird:
    def fly(self):
        raise NotImplementedError

# 자식 클래스
class Eagle(Bird):
    # pass
    # 메서드 재정의
    pass
    def fly(self):
        print("very fast")

eagle = Eagle()
eagle.fly()

# 예외 만들기
class MyError(Exception):
    pass

def say_nick(nick):
    if nick == '하하':
        raise MyError()
    print(nick)

try:
    say_nick('호호')
    say_nick('하하')
except MyError as e:
    print(e)