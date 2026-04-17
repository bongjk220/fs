# 변수 스코프
def my_function():
    func_var = "함수 안의 변수"

my_function()

if True:
    if_var = "if문 안의 변수"
    
print(if_var)

for i in range(3):
    for_var = "for문 안의 변수"

print(i)
print(for_var)

with open("py_basic/ch06_입출력/test.txt", "w") as f:
    content = "Hello,  Python!"
    f.write(content)

print(content)
'''
if문 안의 변수
2
for문 안의 변수
Hello,  Python!
'''