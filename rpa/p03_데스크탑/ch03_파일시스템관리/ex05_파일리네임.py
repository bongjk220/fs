import os, shutil, re
from pathlib import Path

# 매출보고서2026년01월01일.xlsx
# 매출보고서_2026_01_01.xlsx

DATE_KR = re.compile(r'(.*?)(\d{4})년(\d{2})월(\d{2})일(.*)')
'''
r (Raw String): 백슬래시(\)를 이스케이프 문자(Escape character)로 처리하지 않고 문자 그대로 인식하도록 지정합니다.
(.*?) (그룹 1): 날짜 앞에 나오는 모든 문자열을 의미합니다. ?가 붙어 필요한 최소한의 문자만 매칭(Lazy 매칭)합니다.
    - . : 아무 문자 1개
    - * : 0개 이상의 반복
    - + : 1개 이상의 반복
    - ? : 필요한 최소한의 문자만 매칭
    ex) "매출보고서" 부분을 매칭합니다.
(\d{4})년 (그룹 2): 숫자(\d) 4자리와 '년'이라는 글자를 매칭합니다. (예: 2026년)
    - \d{4} : 숫자 4자리
    - {4} : 정확히 4번 반복
(\d{2})월 (그룹 3): 숫자(\d) 2자리와 '월'이라는 글자를 매칭합니다. (예: 05월)
    - \d{2} : 숫자 2자리
    - {2} : 정확히 2번 반복
(\d{2})일 (그룹 4): 숫자(\d) 2자리와 '일'이라는 글자를 매칭합니다. (예: 13일)
(.*) (그룹 5): 날짜 뒤에 오는 나머지 모든 문자열을 매칭합니다.
    - . : 아무 문자 1개
    - * : 0개 이상의 반복
    ex) "보고서.xlsx" 부분을 매칭합니다.
'''
def rename_dates(root: Path):

    for folder, _, files in os.walk(root):
        p = Path(folder)

        for name in files:
            match = DATE_KR.fullmatch(name)

            if not match:
                continue

            pre, yyyy, mm, dd, suf = match.groups()

            new_name = f"{pre}_{yyyy}-{mm}-{dd}{suf}"

            dst = p / new_name

            n = 1
            while dst.exists():
                dst = p / f"{dst.stem}_{n}{dst.suffix}"
                n += 1
            src = p / name

            shutil.move(str(src), str(dst))
            print(f"[리네임] {name} -> {dst.name}")

if __name__ == "__main__":
    # base = Path.cwd() / "연습" / "날짜정리"
    base = Path(__file__).parent / "연습" / "날짜정리" # c:\bong\git\fs\rpa\p03_데스크탑\ch03_파일시스템관리\연습\날짜정리
    rename_dates(base)