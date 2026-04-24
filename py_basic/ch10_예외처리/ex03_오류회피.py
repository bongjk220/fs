# import os

# # 현재 실행 중인 파일(ex03_오류회피.py)의 절대 경로를 가져온다.
# current_dir = os.path.dirname(__file__)
# print(current_dir) # c:\bong\git\fs\py_basic\ch10_예외처리

# students = ["김철수", "이영희", "박민수", "최유진"]

# for student in students:
#     # 현재 폴더 경로와 파일명을 결합
#     file_path = os.path.join(current_dir, f"{student}_성적.txt")
#     try:
#         with open(file_path, 'r', encoding="utf-8") as f:
#             score = f.read()
#             print(f"{student}의 성적: {score}")
#     except FileNotFoundError:
#         print(f"{student}의 성적 파일이 없습니다. 건너뜁니다.")
#         pass
#         continue  # 다음 학생으로 넘어감
'''
김철수의 성적: 90점
이영희의 성적 파일이 없습니다. 건너뜁니다.
박민수의 성적: 80점
최유진의 성적 파일이 없습니다. 건너뜁니다.
'''


# 파이썬 3.4+ 
from pathlib import Path

students = ["김철수", "이영희", "박민수", "최유진"]

# 현재 파일의위치를 기준으로 상대 경로 설정
current_dir = Path(__file__).parent
print(current_dir) # c:\bong\git\fs\py_basic\ch10_예외처리

for student in students:
    # / 연산자를 통해 경로를 합친다.
    file_path = current_dir /  f"{student}_성적.txt"
    try:
        with open(file_path, 'r', encoding="utf-8") as f:
            score = f.read()
            print(f"{student}의 성적: {score}")
    except FileNotFoundError:
        print(f"{student}의 성적 파일이 없습니다. 건너뜁니다.")
        pass
        continue  # 다음 학생으로 넘어감

