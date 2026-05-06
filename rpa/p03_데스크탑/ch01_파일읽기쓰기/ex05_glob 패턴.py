# glob 패턴으로 여러 파일 다루기
'''
data?.txt -> data1.txt, data2.txt, data3.txt
data*.txt -> data?????.txt
'''
from pathlib import Path

docs_dir = Path(__file__).parent / "문서"

# 테스트 파일 생성
for i in range(1, 6):
    with open(docs_dir / f"test{i}.txt", "w", encoding="utf-8") as f:
        f.write(f"{i}번째 보고서 내용입니다.\n")

# glob 패턴으로 txt 파일 모두 찾기
for file in docs_dir.glob("test*.txt"):
    print(file)

    with open(file, "r", encoding="utf-8") as f:
        print(f"{file.name} 내용:")
        print(f.read())