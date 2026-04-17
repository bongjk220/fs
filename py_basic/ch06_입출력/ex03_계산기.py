# 계산기
print("===== 간단한 계산기 ====")

# 사용자로부터 두 숫자 입려받기
num1 = int(input("숫자1: "))
num2 = int(input("숫자2: "))

# 계산 결과 출력
print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")
if num2 != 0:
    print(f"{num1} / {num2} = {num1 / num2}")
    print("%d %% %d = %d", (num1, num2, num1 % num2))
    print("%d // %d = %d", (num1, num2, num1 // num2))
    print("%d ** %d = %d", (num1, num2, num1 ** num2))
else:
    print("0으로 나눌 수 없습니다.")
'''
숫자1: 4
숫자2: 5
%d + %d = %d (4, 5, 9)
%d - %d = %d (4, 5, -1)
%d * %d = %d (4, 5, 20)
%d / %d = %d (4, 5, 0.8)
%d %% %d = %d (4, 5, 4)
%d // %d = %d (4, 5, 0)
%d ** %d = %d (4, 5, 1024)
'''

