# r(Raw String) : 날 머신 문자열
target_path = r"C:\bong\git\fs\py_basic\ch06_입출력" # "C:\\bong\\git\\fs\\py_basic\\ch06_입출력"
base_path = r"C:\bong\git\fs"
relative_path = "py_basic/ch06_입출력"
full_path = base_path + "/" + relative_path

#target_path = "C:/bong/git/fs/py_basic/ch06_입출력"
#base_path = r"C:/bong/git/fs"
#relative_path = "py_basic/ch06_입출력"
#full_path = base_path + "/" + relative_path

print(target_path)
print(base_path)
print(relative_path)
print(full_path)

# with를 사용하지 않았을 경우
f = open(full_path+"/foo1.txt", "w")
f.write("Life is too short, you need python")
f.close()

# 파일 읽기
f = open(full_path+"/foo21.txt", "r")
data = f.read()
print(data)
f.close

# with 문
# 자동으로 닫는다.(close문이 없다.)
with open(full_path+"/foo2.txt", "w") as f:
    f.write("Life is too short, you need python")

# 파일 읽기
f = open(full_path+"/foo2.txt", "r")
data = f.read()
print(data)
f.close