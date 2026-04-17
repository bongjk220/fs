# 
def add_and_mul(a, b):
    return a+b, a*b

result =  add_and_mul(3,4)
print(result) # (7, 12)

# 튜플
# a, b = (7, 12)
# a, b = 7, 12 #가로 생략가능
result1, result2 =  add_and_mul(3,4)
print(result1, result2) # 7, 12
print(result1) # 7
print(result2) # 12

def add_and_mul2(a, b):
    return a+b
    return a*b # 죽은 코드

result = add_and_mul2(2,3)
print("--------------")
print(result) # 5


def say_nick(nick):
    if nick == "야동":
        return
    print("나의 별명은 %s 입니다. " % nick)

say_nick('야구') # 나의 별명은 야구 입니다.
say_nick('야동')

