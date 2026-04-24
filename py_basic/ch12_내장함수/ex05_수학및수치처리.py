
#########################################################
# 1. 기본 산술 및 절대값
#########################################################
# # abs
# abs(x)는 숫자를 입력받아 그 숫자의 절댓값을 반환
print(abs(3)) # 3
print(abs(-3)) # 3
print(abs(-1.2)) # 1.2

# divmod
# divmod(a, b)는 2개의 숫자 a, b를 입력으로 받아
# a를 b로 나눈 몫과 나머지를 튜플로 반환
print(divmod(7,3)) # (2, 1)
print(7 // 3) # 2 (몫)
print(7 % 3) # 1 (나머지)

# pow
# pow(x, y)는 x를 y제곱한 결괏값을 반환
print(pow(2, 4)) # 16
print(pow(3, 3)) # 27
print(2 ** 4) # 2*2*2*2 = 16
print(pow(2, 4, 3)) # 16을 3으로 나눈 나머지 1 -> 2*2*2*2 % 3 = 1

print('='*80)
#########################################################
# 2. 반올림 및 수치 정밀도
#########################################################
# round
# round(number [,ndigits])는 숫자를 입력받아 반올림해 반환
# 오사오입?
print('round(2.5) = ',round(2.5)) # 2
print('round(3.5) = ',round(3.5)) # 4

print(round(4.6)) # 5
print(round(4.2)) # 4
print(round(5.678, 2)) # 5.68

print('-'*60)
# ---------------------------------------------
# math
# ---------------------------------------------
import math

n = 3.556

print(round(n, 2))   # 3.56 (소수점 둘째자리까지 반올림)
print(math.ceil(n))   # 4
print(math.floor(n))  # 3

print('='*80)
#########################################################
# 3. 집계 및 비교
#########################################################

# sum
# sum(iterable)은 입력 데이터의 합을 반환
print(sum([1,2,3])) # 6
print(sum((4,5,6))) # 15
print(sum({4,5,6})) # 15
# print(sum(4,5,6)) # TypeError
print(sum({4:"a", 5:"b", 6:"c"})) # 15

# max
# max(iterable)는 반복 가능한 데이터를 입력받아 최댓값을 반환
print(max([1,2,3])) # 3
print(max("python")) # y
print(max("파이썬")) # 파

# min
# min(iterable)는 max 함수와 반대로,
# 반복 가능한 데이터를 입력받아 최솟값을 반환
print(min([1,2,3])) # 1
print(min("python")) # h
print(min("파이썬")) # 썬

print('-'*60)
# ---------------------------------------------
# numpy
# ---------------------------------------------
import numpy as np
from scipy import stats

data = [10, 20, 20, 30, 1000] # 1000이라는 이상치가 포함됨
mode_result = stats.mode(data, keepdims=True)

print(f"산술 평균: {np.mean(data)}")   # 216.0 (이상치 때문에 높게 나옴)
print(f"중앙값: {np.median(data)}")     # 20.0 (실제 데이터의 중심을 더 잘 반영)
print(f"최빈값: {mode_result.mode[0]}")     # 20
print(f"최빈값: {mode_result.count[0]}")     # 2

print('-'*60)
# ---------------------------------------------
# pandas
# ---------------------------------------------
import pandas as pd

data = [10, 20, 20, 30, 30, 1000]
series = pd.Series(data)

print(f"최빈값: {series.mode()[0]}") # 20
print(f"최빈값: {series.mode()[1]}") # 30

print('-'*60)
# ---------------------------------------------
# statistics
# ---------------------------------------------
import statistics

data = [10, 20, 20, 30, 30, 1000]
print(f"최빈값: {statistics.mode(data)}") # 20

# 모든 최빈값을 리스트로 반환
all_modes = statistics.multimode(data)

print(all_modes)      # [20, 30]
print(all_modes[0])   # 20
print(all_modes[1])   # 30 (이제 [1] 사용 가능!)

print('='*80)
#########################################################
# 4. 진수 변환 (부호 있는 정수 처리)
#########################################################

value = 255

# 10진수(0~9) -> 각 진수 문자열
b_str = bin(value)  # 10진수 -> 2진수(0,1) : '0b11111111'
o_str = oct(value)  # 10진수 -> 8진수(0~7) : '0o377'
h_str = hex(value)  # 10진수 -> 16진수(0~f) : '0xff'


print(f"2진수: {b_str}, 8진수: {o_str}, 16진수: {h_str}")

# 각 진수 문자열 -> 10진수 정수
print(int(b_str, 2))   # 255
# print(int(b_str, 8))   # ValueError
print(int(o_str, 8))   # 255
print(int(h_str, 16))  # 255

# format 함수를 이용한 진수 변환 (숫자만)
print(f"16진수 숫자만: {format(value, 'x')}")  # 'ff'