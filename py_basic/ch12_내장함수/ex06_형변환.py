#########################################################
# 1. 자동(암시적) 형변환
#########################################################

num_int = 10
num_float = 1.5
result = num_int + num_float  # 11.5 (float로 자동 변환)

print(result) # 11.5(float으로 자동 형변환)

print('='*80)
#########################################################
# 2. 강제(명시적) 형변환
#########################################################
# 자료형 변환(Type Conversion)

# int
# int(x)는 문자열 형태의 숫자나 소수점이 있는 숫자를
# 정수로 반환하는 함수이다.
# 정수가 입력되면 그대로 반환한다.
print(int('3')) # 3 (문자열은 정수로 변환)
print(int(3.6)) # 3 (소수점이 있는 숫자는 정수로 변환)

# int(x, radix)는 radix 진수로 표현된
# 문자열 x를 10진수로 변환하여 반환한다.
print(int('11', 2)) # 3
print(int('1A', 16)) # 26

# str
# str(object)는 객체를 문자열 형태로 변환하여 반환
print(str(3)) # 3
print(str('hi')) # hi

# list
# list(iterable)는 반복 가능한 데이터를 입력받아 리스트로 만들어 반환
print(list("python")) # ['p', 'y', 't', 'h', 'o', 'n']
print(list((1, 2, 3))) # [1, 2, 3]

a = [1, 2, 3]
b = list(a)
print(b) # [1, 2, 3]

# tuple
# tuple(iterable)은 반복 가능한 데이터를 튜플로 바꾸어 반환하는 함수
# 입력이 튜플인 경우에는 그대로 반환한다.
print(tuple("abc")) # 문자열 -> 튜플 : ('a','b','c')
print(tuple([1,2,3])) # 리스트 -> 튜플 : (1, 2, 3)
print(tuple((1,2,3))) # 튜플 -> 튜플 : (1, 2, 3)

# chr
# chr(i)는 유니코드 숫자 값을 입력받아 그 코드에 해당하는 문자를 반환
# 유니코드는 전 세계의 모든 문자를 컴퓨터에서
# 일관되게 표현하고 다룰 수 있도록 설계된 산업 표준 코드이다.
print(chr(49)) # 1  <--이정도는 알자
print(chr(54)) # 6
print(chr(55)) # 7
print(chr(56)) # 8
print(chr(57)) # 9
print(chr(58)) # :
print(chr(59)) # ;
print(chr(60)) # <
print(chr(61)) # =
print(chr(62)) # >
print(chr(63)) # ?
print(chr(64)) # @
print(chr(65)) # A <--이정도는 알자
print(chr(90)) # Z
print(chr(91)) # [
print(chr(92)) # \
print(chr(93)) # ]
print(chr(94)) # ^
print(chr(95)) # _
print(chr(96)) # `
print(chr(97)) # a  <--이정도는 알자
print(chr(100)) # d
print(chr(44032)) # 가
print(chr(44033)) # 각

# ord
# ord(c)는 문자의 유니코드 숫자 값을 반환
print(ord('a')) # 97
print(ord('A')) # 65
print(ord('1')) # 49
print(ord('가')) # 44032