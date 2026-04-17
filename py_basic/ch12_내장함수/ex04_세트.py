# set 내장 함수
# add() : 요소 추가
s1 = set([1,2,3])
s1.add(4)
print(s1) # {1, 2, 3, 4}

# update() : 여러 요소 추가
s1.update([5,6,7])
print(s1) # {1, 2, 3, 4, 5, 6, 7}

# remove() : 요소 제거
s1 =  set([10,20,30])
s1.remove(20)
print(s1) # {10, 30}
# s1.remove(40) # KeyError: 40 -> 존재하지 않는 요소 제거 시 에러 발생

# discard() : 특정 요소 제거(존재하지 않는 요소 제거 시 에러 발생x)
s1 =  set([10,20,30])
s1.discard(20)
print(s1) # {10, 30}
s1.discard(40) # 존재하지 않는 요소 제거 시 에러 발생x
print(s1) # {10, 30}

# clear() : 모든 요소 제거
s1 =  set([10,20,30])
s1.clear()
print(s1) # set() -> 빈 set

# pop() : 임의의 요소 제거 후 반환
s1 =  set([10,20,30])
item = s1.pop()
print(item) # 10 -> 제거된 요소 반환
print(s1) # {20, 30} -> 제거된 요소 제외한 나머지 요소 출력



