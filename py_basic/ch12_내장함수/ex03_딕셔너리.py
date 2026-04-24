# 파이썬 3.11.2 버전
'''
시퀀스타입: 리스트와 튜플의 차이점 : 수정이 가능하냐 안하냐, 중가로 -> 순서(인덱스) 있다.
    리스트 : [item1, item2, ...]]
    튜플 : ()
매핑 타입 : 딕셔너리 -> 순서 없다. -> 순서있다(파이썬 3.7+ 이후로 있다)
    딕셔너리 : {키1 : 값1, 키2 : 값2, ... }
'''

di1 = {
    'name':'hong',
    'age':30,
    'phone':'010-1234-56789',
    'birth':'1118',
    'email': ''
}

# 딕셔너리 쌍(키:값) 추가히기
a = {1:'a'}
# 딕셔너리명[키] = 값
a[2] = 'b'
print(a) # {1: 'a', 2: 'b'}
a['name'] = 'hong'
print(a)   # {1: 'a', 2: 'b', 'name': 'hong'}
a[3] = [1,2,3]
print(a)  # {1: 'a', 2: 'b', 'name': 'hong', 3: [1, 2, 3]}

# 키(key)를 사용하여 값(value) 얻기
grade = {'pey':10, 'julliet':99}
print(grade['pey']) #10
print(grade['julliet']) #99

# 키는 중복될 수 없다.
a = {1: 'a', 1:'b', 1:'c'}
print(a)

# 리스트는 키로 사용 불가
# a = { [1,2]: 'hi'} # error
a = { 'name': [1,2]}
print(a)

# 함수
# keys()
# values()
# items()

a = {
    'name':'hong',
    'age':30,
    'phone':'010-1234-56789',
    'birth':'1118',
    'email': ''
}

# clear : 모든 아이템 삭제
# get : key로 value얻기
print(a['name']) # hong
# get
print(a.get['name']) # hong
# 없는키를 사용하면
# print(a.[]) # error
print(a.get('zipcode')) # None

# get(키, 기본값(default값))
print(a.get('address', '경기도 성남시 분당구')) #성남시 분당구
print(a.get('zipcode', '12820')) # 12820

# in 키워드 : 키의 유무, 있으면 True, 없음 False
print('name' in a) # True
print('zipcode' in a) # False

# keys(), values(), items()
print(a.keys()) # dict_keys(['name', 'age', 'phone', 'birth', 'email'])
print(a.values()) # dict_values(['hong', 30, '010-1234-56789', '1118', ''])
print(a.items()) # dict_items([('name', 'hong'), ('age', 30), ('phone', '010-1234-56789'), ('birth', '1118'), ('email', '')])

# pop(키) : 키로 값얻기(잘라내기)
# email = a.pop('email') # KeyError
print(a.pop('name')) # hong
print(a.pop('email','정보없음')) # 정보없음
print(a) # {'age': 30, 'phone': '010-1234-56789', 'birth': '1118', 'email': '', 'zipcode': None}

# popitem() : 가장 최가로 이상한 아이템 삭제
print(a.popitem()) # ('email', '')
print(a) # {'age': 30, 'phone': '010-1234-56789', 'birth': '1118', 'zipcode': None}

# update(딕셔너리) : 합치기
a = {1:'a', 2:'b'}
b = {3:'c', 4:'d'}
a.update(b)
print(a) # {1: 'a', 2: 'b', 3: 'c', 4: 'd'}

