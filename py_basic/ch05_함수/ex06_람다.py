def add(a,b):
    '''
    함수명 = lambda 매개변수1, 매개변수2: 리턴값
    '''
    return a+b

result = add(3,4)
print(result) # 7

#독스트링(Docstring)
print(add.__doc__)

# lambda(람다) 예약어
'''
    함수명 = lambda 매개변수1, 매개변수2: 리턴값
'''
add = lambda a, b: a+b

result = add(3,4)
print(result) # 7

