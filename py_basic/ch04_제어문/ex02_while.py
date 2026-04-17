# 반복문
# while 문
# do~while문은 없다.
'''
    while 조건문:
    
'''

tree_hit = 0
while tree_hit < 10:
    tree_hit += 1 # tree_hit = tree_hit + 1
    #print(f"나무를 {tree_hit}번 찍었습니다.")
    print(f"나무를 %d번 찍었습니다.", tree_hit)
    if tree_hit == 10:
        print("나무 넘어갑니다.")

prompt="""
1. add
2. Del
3. list
4. quit
Enter number: 
1"""

# int() : 정수
# input() : 사용자 입력
'''
number = 0
while number != 4:
    print(prompt)
    number = int(input(prompt))
'''

# break 문
# - break 무한반복문을 탈출한다.
# 커피 자판기
# 터미널 실행중지 : Ctrl + C
'''
coffee = 10
money = 300
while True:
    money = int(input("돈을 넣어 주세요: "))
    if money == 300:
        print("커피를 줍니다.")
        print(f"남은 커피의 양은 {coffee}잔입니다.")
        coffee -= 1
    elif money > 300:
        print(f"거스름돈 {money - 300}원을 주고 커피를 줍니다.")
        coffee -= 1
    else:
        print(f"돈 {money}원을 다시 돌려주고 커피를 주지 않습니다.")
        print(f"남은 커피의 양은 {coffee}잔입니다.")
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break
'''
        
# continue 문
# - continue 반복문을 계속 진행한다.
a = 0
while a < 10:
    a += 1
    if a % 2 == 0: continue # 짝수이면 아래 문장을 실행하지 않고 다시 반복문으로 올라간다.
    print(a)

# while~else 문
count = 0
while count < 3:
    print(f"카운트 : {count}")
    count += 1
else:
    print("while 문이 정상 종료되었습니다.")

# break 문으로 while문을 탈출하면 else 절은 실행되지 않는다.
count = 0
while count < 5:
    if count == 2:
        break
    print(f"카운트:{count}")
    count += 1
else:
    print("while 문이 정상 종료되었습니다.")

# 중첩 while문
i = 1
while i <= 3:
    j = 1
    while j <= 3:
        print(f"i: {i}, j: {j}")
        j+=1
    i+=1
else:
    print("while 문이 정상 종료되었습니다.")

# 