'''
중간 파일을 지운 후 새로운 파일이 생길 경우
a_1.txt
a_2.txt
a_3.txt
에서 a_2.txt를 지운 후에 새로운 파일 a_2.txt가 생기면

a_1.txt
a_2.txt -> 최근에 생긴 파일이 중간에 들어감
a_3.txt

새로운 파일 a_2.txt가 생기면
a_3.txt를 a_2.txt로 바꾸고, a_2.txt를 a_3.txt로 지정

파일 정렬 시
a_1.txt
a_2.txt
a_3.txt
a_11.txt 가 생기면

a_1.txt
a_11.txt
a_2.txt
a_3.txt 가 되므로

a_001.txt
a_002.txt
a_003.txt
a_011.txt
'''

# a = 1
# s = str(a).zfill(3)
# print(s) # 001

import shutil
from pathlib import Path

def renumber(folder: Path, prefix: str = "spam", ext: str = ".txt"):
    folder.mkdir(parents=True, exist_ok=True)

    # 연습/번호정리 파일생성 --> 없어서 추가
    for name in ["spam001.txt", "spam103.txt", "spam015.txt"]:
        (folder / name).write_text(f"{name}샘플", encoding="utf-8")

    files = sorted(folder.glob(f"{prefix}[0-9][0-9][0-9]{ext}")) # spam???.txt
    # folder.glob(...): 지정된 패턴(예: spam001.txt)과 일치하는 파일들을 모두 찾습니다.

    temps = []

    for i, f in enumerate(files, start=1): # 파일 리스트를 돌면서 1번부터 순번을 매깁니다.
        print(f"{i}/{f}")
        tmp = folder / f"__tmp_{i}{ext}"
        print(f"{tmp}")
        shutil.move(f, tmp) # 파일을 일단 __tmp_1.txt 처럼 전혀 다른 임시 이름으로 바꿉
        temps.append(tmp)
        print(f"temps:{temps}")
    
    for i, tmp in enumerate(sorted(temps), start=1):
        new = folder / f"{prefix}{str(i).zfill(3)}{ext}" # - `str(i).zfill(3)`: 숫자 `1`을 `001`로 변환하여 3자리 고정 폭을 만듭니다.
         # 결과적으로 중간에 번호가 비어 있었더라도 `001`, `002`, `003` 순서대로 빈틈없이 이름이 정렬
        print(f"new:{new}")
        shutil.move(str(tmp), str(new))
        print(f"[이름정리]{new.name}")


if __name__ == "__main__":
    # base = Path.cwd() / "연습" / "번호정리"
    base = Path(__file__).parent / "연습" / "번호정리" # c:\bong\git\fs\rpa\p03_데스크탑\ch03_파일시스템관리\연습\번호정리
    # base.mkdir(parents=True, exist_ok=True)

    renumber(base)