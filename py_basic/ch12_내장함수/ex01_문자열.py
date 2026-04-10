# 문자열 내장함수
# count('문자열') : 문자열 내에서 특정 문자열의 개수 세기
a = "hobby"
print(a.count('b')) # 문자열 내에서 'b'의 개수 세기

# find('문자열') : 문자열 내에서 특정 문자열이 처음으로 나온 위치 반환 (인덱스)
a = "Python is the best choice"
print(a.find('b')) # 문자열 내에서 'b'의 위치 반환
print(a.find('k')) # 문자열 내에서 'k'가 없으므로 -1 반환

# index('문자열') : 문자열 내에서 특정 문자열이 처음으로 나온 위치 반환 (인덱스), find와 달리 문자열이 없으면 오류 발생
a = "Life is too shoot,You need python"
print(a.index('t')) # 문자열 내에서 't'의 위치 반환, find와 달리 문자열이 없으면 오류 발생
#print(a.index('k')) # 문자열 내에서 'k'가 없으므로 오류 발생

# join() : 문자열을 합칠 때 사용
print(",".join('abcd')) # 'a', 'b', 'c', 'd' -> 문자열 'abcd'의 각 문자 사이에 ','를 넣어서 하나의 문자열로 반환

# upper() : 문자열을 모두 대문자로 변환
a = "hi"
print(a.upper()) # 문자열을 모두 대문자로 변환

# lower() : 문자열을 모두 소문자로 변환
a = "HI"
print(a.lower()) # 문자열을 모두 소문자로 변환

# strip() : 문자열 양쪽의 공백 제거
a = "   hello   "
print(a.strip()) # 문자열 양쪽의 공백 제거
print(a.lstrip()) # 문자열 왼쪽의 공백 제거
print(a.rstrip()) # 문자열 오른쪽의 공백 제거
print(len(a.strip())) # 문자열 양쪽의 공백 제거 후 문자열 길이 반환
print(len(a.lstrip())) # 문자열 왼쪽의 공백 제거 후 문자열 길이 반환
print(len(a.rstrip())) # 문자열 오른쪽의 공백 제거 후 문자열 길이 반환

# replace(이전문자열, 새로운문자열) : 문자열 내에서 특정 문자열을 다른 문자열로 대체
a = "Life is too short,You need python"
print(a.replace("short", "long")) # 문자열 내에서 'short'을 'long'으로 대체
print(a.replace("o", "0")) # 문자열 내에서 'o'를 '0'으로 대체
print(a.replace(" ", "")) # 문자열 내에서 공백을 제거
print(a.replace(" ", "\n")) # 문자열 내에서 공백을 줄바꿈으로 대체

# split() : 문자열을 특정 구분자로 나누어서 리스트로 반환
a = "Life is too short,You need python"
print(a.split()) # 문자열을 공백을 기준으로 나누어서 리스트로 반환
print(a.split(",")) # 문자열을 ','를 기준으로 나누어서 리스트로 반환
b = "a,b,c,d"
print(b.split(",")) # 문자열을 ':'를 기준으로 나누어서 리스트로 반환

# 논리값 출력 함수
# 형태 : isXXX()
# isalpha() : 문자열이 모두 알파벳으로 구성되어 있는지 확인
a = "Python"
print(a.isalpha()) # True - 문자열이 모두 알파벳으로 구성되어 있는지 확인
b = "Python3"
print(b.isalpha()) # False - 문자열이 모두 알파벳으로 구성되어 있는지 확인
a = "HelloPython!"
print(a.isalpha()) # False - 문자열이 모두 알파벳으로 구성되어 있는지 확인

# isdigit() : 문자열이 모두 숫자로 구성되어 있는지 확인
a = "12345"
print(a.isdigit()) # True - 문자열이 모두 숫자로 구성되어 있는지 확인
b = "12삼45"
print(b.isdigit()) # False - 문자열이 모두 숫자로 구성되어 있는지 확인
a = "12.45"
print(a.isdigit()) # False - 문자열이 모두 숫자로 구성되어 있는지 확인

# startswith('문자열') : 문자열이 특정 문자열로 시작하는지 확인
a = "Life is too shoot"
print(a.startswith("Li")) # True - 문자열이 'Life'으로 시작하는지 확인
print(a.startswith("life")) # False - 문자열이 'life'으로 시작하는지 확인 (대소문자 구분)

# endswith('문자열') : 문자열이 특정 문자열로 끝나는지 확인
print(a.endswith("short")) # True - 문자열이 'short'로 끝나는지 확인
print(a.endswith("Short")) # False - 문자열이 'Short'로 끝나는지 확인 (대소문자 구분)
