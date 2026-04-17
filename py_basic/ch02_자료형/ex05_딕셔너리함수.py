# 딕셔너리 관련 함수
'''
    {key : value}

'''
a = {
    'name': 'hong',
    'age': 20,
    'phone': '010-1234-5678',
    'birth': '1118',
    'address': '성남시 분당구'
}

# keys()
print(a.keys()) # dict_keys(['name', 'age', 'phone', 'birth'])
print(list(a.keys())) # ['name', 'age', 'phone', 'birth']

# values()
print(a.values()) # dict_values(['hong', 20, '010-1234-5678', '1118'])
print(list(a.values())) # ['hong', 20, '010-1234-5678', '1118']

# items()
print(a.items()) # dict_items([('name', 'hong'), ('age', 20), ('phone', '010-1234-5678'), ('birth', '1118')])
print(list(a.items())) # [('name', 'hong'), ('age', 20), ('phone', '010-1234-5678'), ('birth', '1118')]

# get() : key로 value얻기
# key로 value얻기
print(a['name'])
# get()
print(a.get('name'))

# 없는 키를 사용하면
#print(a['address']) # error
print(a.get('address')) #None

# get(키, [기본값])
print(a.get('address2', '경기도 성남시 분당구')) #경기도 성남시 분당구

# in 키워드 : 키의 유무, 있으면 True, 없으면 False
print('name' in a) # True
print('zipcode' in a) # False

# pop(키) - 잘라내기
phone = a.pop('phone')
print(phone)  # 010-1234-5678
print(a) # {'name': 'hong', 'age': 20, 'birth': '1118', 'address': '성남시 분당구'}

email = a.pop('email','정보없음')
print(email) # 정보없음
print(a) # {'name': 'hong', 'age': 20, 'birth': '1118', 'address': '성남시 분당구'}

# clear() : 아이템 삭제
a.clear()
print(a) # {}

