'''
윈도우: "c:\\", r"c:\", "c:/"
맥, 리눅스: /users/home/...
'''

# 내장모듈 : pathlib
from pathlib import Path

# 현재 작업 폴더
cur_dir = Path.cwd()
print("현재 작업 디렉토리: ", cur_dir)

# 홈 디렉토리
home_dir = Path.home()
print("홈 디렉토리: ", home_dir)

# 경로 이어 붙이기
보고서_dir = cur_dir / "문서" / "보고서.txt"
print("보고서 경로: ", 보고서_dir)

# 상대경로 -> 절대 경로
rel_path = Path("data/학생명단.txt")
print("상대 경로: ", rel_path)
print("절대 경로: ", rel_path.resolve())

# 경로 속성
sample_file = Path("c:/users/홍길동/음악/노래.mp3")
print("파일 이름:", sample_file.name)
print("확장자:", sample_file.suffix)
print("파일명만:", sample_file.stem)
print("디렉토리:", sample_file.parent)
print("드라이브:", sample_file.drive)

# 파일 존재 여부
print("파일 존재 여부: ", sample_file.exists()) # False
