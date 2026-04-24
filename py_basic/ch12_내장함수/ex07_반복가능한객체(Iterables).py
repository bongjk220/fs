#########################################################
# 1. map
#########################################################
# map(function, iterable)은 함수와 반복 가능한 데이터를 입력으로 받는다.
# 입력받은 데이터의 각 요소에 함수를 적용한 결과를 반환
# map 함수는 map 객체를 반환한다.
# 기존 데이터를 새로운 데이톨 변환

# 리스트를 입력받아 각 요소에 2를 곱해 반환하는 함수
def two_times(numberList):
    result = []
    for number in numberList:
        result.append(number * 2)
    return result

# 1. 맵을 사용하지 않은 케이스
result = two_times([1, 2, 3, 4])
print('1 = %s' % result) # [2,4,6,8]

# 2. 맵을 사용한 케이스
def two(x):
    return x * 3

print('2 = %s' % list(map(two, [1, 2, 3, 4]))) # [3, 6, 9, 12]
print('2_1 = %s' % map(two, [1, 2, 3, 4])) # <map object at 0x000001F898117D60>

# 3. lambda 사용
print('3 = %s' % list(map(lambda a: a*4, [1, 2, 3, 4]))) # [4, 8, 12, 16]

print('='*80)
#########################################################
# 2. filter
#########################################################
# filter란 '무엇인가를 걸러 낸다'라는 뜻
# filter(함수, 반복_가능한_데이터)
# 반복 가능한 데이터의 요소를 순서대로 함수에 전달하여
# 반환값이 참인 것만 묶어서 반환한다.

# positive는 리스트를 입력받아 각 요소를 판별해서 양수 값만 반환
def positive(lists):
    result = []
    for i in lists:
        if i > 0:
            result.append(i)
    return result

print(positive([1,-3,2,0,-5,6])) # [1, 2, 6]

def positive(x):
    return x > 0

# list 함수는 filter 함수의 반환값을 리스트로 출력하기 위해 사용했다.
print(list(filter(positive, [1,-3,2,0,-5,6]))) # [1,2,6]

# lambda 사용
print(list(filter(lambda x: x > 0, [1,-3,2,0,-5,6]))) # [1,2,6]

#########################################################
# 3.  요소 조합 및 인덱스
#########################################################
# zip : 대응되는것끼리 묶는다.
# zip(*iterable)은 동일한 개수로 이루어진 데이터들을 묶어서 반환
print(zip([1,2,3,4], [4,5,6])) # <zip object at 0x0000027CEBA41F00>
print(list(zip([1,2,3,4], [4,5,6]))) # [(1, 4), (2, 5), (3, 6)] 대응안되는것은 무시
print(list(zip([1,2,3],[4,5,6],[7,8,9]))) # [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
print(list(zip("abc", "def"))) # [('a', 'd'), ('b', 'e'), ('c', 'f')]

print('-'*60)
# enumerate
# enumerate는 '열거하다'라는 뜻이다.
# 순서가 있는 데이터(리스트, 튜플, 문자열)를 입력으로 받아
# 인덱스 값을 포함하는 enumerate 객체를 반환
# 보통 enumerate 함수는 for 문과 함께 사용한다.
# 자료형의 현재 순서(index)와 그 값을 쉽게 알 수 있다.
for i, name in enumerate(['body', 'foo', 'bar']):
    print(i, name)
'''
0 body
1 foo
2 bar
'''

print('='*80)
#########################################################
# 5. sorted
#########################################################
# sorted(iterable)는 입력 데이터를 정렬한 후 그 결과를 리스트로 반환
lst = [3,1,2]

print(lst) # [3,1,2]
print(sorted(lst)) # [1, 2, 3] > 원본은 놔두고 바꾼다.
print(lst.sort()) # None 
print(lst) #  [1, 2, 3] -> 아예 데이터를 바꿔버린다.

print(sorted(['a','c','b'])) # ['a','b','c']
print(sorted("zero")) # ['e','o','r','z']
print(sorted((3, 2, 1))) # [1, 2, 3]

print('-'*60)
# 리스트 뒤집기
# reversed(sequence) : 순서대로 데이터를 뒤집기 위한 객체를 반환
numbers = [1, 2, 3, 4, 5]
rev_numbers = reversed(numbers)
print(list(rev_numbers)) # 출력: [5, 4, 3, 2, 1] > 원본은 놔두고 바꾼다.
print(numbers) # [1, 2, 3, 4, 5] # 원본은 그대로
print(numbers.reverse()) # None
print(numbers) # [5, 8, 4, 3, 2, 1] > 아예 데이터를 바꿔버린다.

# 문자열 뒤집기
text = "Python"
rev_text = reversed(text)
print("rev_text = ", rev_text)  # <reversed object at 0x0000021DF2BDBFD0>
print("-".join(rev_text)) # n-o-h-t-y-P  > join문을 하면 위치 정보가 바뀐다.
print("rev_text = ", rev_text)  # <reversed object at 0x0000021DF2BDBFD0>
print(list(rev_text)) # ['n', 'o', 'h', 't', 'y', 'P']  > 예상이었지만 [] 가 된다.
print("rev_text = ", rev_text)  # <reversed object at 0x0000021DF2BDBFD0>
print("".join(rev_text)) # nohtyP

# 반복문(for)에서의 활용
fruits = ["사과", "배", "포도"]
for fruit in reversed(fruits):
    print(fruit)
'''
포도
배
사과
'''

print('='*80)
#########################################################
# 7. 논리 판단 (Any & All)
#########################################################

# all
# all(x)는 반복 가능한 데이터 x를 입력값으로 받아
# x의 요소가 모두 참이면 True,
# 거짓이 하나라도 있으면 False를 반환한다.
# 반복 가능한 데이터란?
# for 문에서 사용할 수 있는 자료형을 의미한다.
# 리스트, 튜플, 문자열, 딕셔너리, 집합 등이 있다.
print(all([1,2,3])) # True
# 요소 0은 거짓
print(all([0,2,3])) # False
# all의 입력 인수가 빈 값인 경우에는 True를 반환한다.
#print(all(0)) # Error > Iterable만 가능하므로 에러
print(all("")) # True
print(all([])) # True
print(all(())) # True
print(all({})) # True
print(all(set())) # True
# print(all(None)) # Error
# print(all(False)) # Error
print(all([0])) # False 인자로 사용하면 False
print(all([""])) # False 인자로 사용하면 False
print(all([[]])) # False 인자로 사용하면 False
print(all([()])) # False 인자로 사용하면 False
print(all([{}])) # False 인자로 사용하면 False
print(all([set()])) # False 인자로 사용하면 False
print(all([None])) # False 인자로 사용하면 False


print('-'*60)
# any
# any(x)는 반복 가능한 데이터 x를 입력으로 받아
# x의 요소 중 하나라도 참이 있으면 True를 반환하고,
# x가 모두 거짓일 때만 False를 반환한다.
# 즉, all(x)의 반대로 작동한다.
print(any([1, 2, 3, 0])) # True
print(any([0, ""])) # False
print(any([])) # False