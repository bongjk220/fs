# 1. 파일 생성하기
'''
    파일 열기  모드
        r : read(읽기)
        w : write(쓰기)
        a : append(추가)
'''
# 절대경로
'''
    http://~
    https://~
    C:~
    D:~
'''
# f = open("C:\\bong\\git\\fs\\py_basic\\ch06_입출력\\newfile.txt", "w")
# f = open("C:/bong/git/fs/py_basic/ch06_입출력/newfile.txt", "w")

# 상대경로
f = open("py_basic/ch06_입출력/newfile.txt", "w", encoding="utf-8")
f.write("Life is too short!\n")
f.close()    # 파일을 쓰기 모드로 열기

# 2. 파일 읽기
f = open("py_basic/ch06_입출력/newfile.txt", "r", encoding="utf-8")
#f = open("py_basic/ch06_입출력/newfile.txt", "r")
data = f.read()
print(data)
f.close

# 3. 파일 쓰기
f = open("py_basic/ch06_입출력/newfile.txt", "a", encoding="utf-8")
for i in range(2, 10):
    for j in range(1, 10):
        data = "%d단 : %d*%d=%d\t" % (i, i, j, i*j)
        f.write(data)
    data = "\n"
    f.write(data)
f.close

print("==========전체 파일 읽기=========")

# 4. 파일 읽기
f = open("py_basic/ch06_입출력/newfile.txt", "r", encoding="utf-8")
data = f.read()
print(data)
f.close

print("==========readline으로 파일 읽기=========")

# 5. readline으로 파일 읽기
f = open("py_basic/ch06_입출력/newfile.txt", "r", encoding="utf-8")
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close

print("==========readlines 파일 읽기=========")

# 6. 한줄씩 읽은것을 모은것
f = open("py_basic/ch06_입출력/newfile.txt", "r", encoding="utf-8")
lines = f.readlines()
print(lines)

print("==========for문 파일 읽기=========")
for line in lines:
    line = line.strip()
    print(line)
f.close()