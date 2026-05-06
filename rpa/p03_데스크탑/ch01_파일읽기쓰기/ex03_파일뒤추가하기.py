from pathlib import Path
from datetime import datetime

today = datetime.now().strftime("%Y%m%d")

# diary_file = Path.home() / "문서" / "일기.txt"
# diary_file = Path.cwd() / "문서" / "일기.txt"
diary_file = Path(__file__).parent / "문서" / f"일기_{today}.txt"

# 디렉토리 생성
diary_file.parent.mkdir(parents=True, exist_ok=True)

# 쓰기 모드: 기존 내용 삭제 후 새로 작성
with open(diary_file, "w", encoding="utf-8") as f:
    f.write("2026-09-08\n") # write()는 줄 바꿈이 없다.
    f.write("오늘은 파이썬 파일쓰기 공부를 했다.\n")
    f.write("생각보다 쉽고 재미있다.\n")

# 추가 모드: 기존 내용 뒤에 덧붙이기
with open(diary_file, "a", encoding="utf-8") as f:
    f.write("저녁에 운동도 했다.\n")

# 읽어서 확인
with open(diary_file, "r", encoding="utf-8") as f:
    print("일기 내용:\n", f.read())
