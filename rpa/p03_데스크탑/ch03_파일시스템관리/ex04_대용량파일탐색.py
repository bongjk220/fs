'''
객체.메서드()
base.resolve() -> 메서드 -> 이유 : base는 객체

이건 메서드 아님
os.walk() -> 함수 -> 이유: os.py는 모듈

os.path.getsize()
'''
import os
from pathlib import Path

def find_big_files(base: Path, size_kb: int = 100):
    # 절대 경로
    base = base.resolve() # 시스템 전체에서 통용되는 절대 경로
    print(base)
    
    size_bytes = size_kb * 1024 # KB 단위를 Byte로 바꾸기 위해 1024를 곱
    
    for folder, _, files in os.walk(base): # os.walk : 하위 폴더를 모두 포함하여 탐색
        p = Path(folder)
        for name in files:
            fp = p / name

            try:
                size = fp.stat().st_size # 파일의 상태 정보를 가져와 그중 크기(Byte) 값을 추출
                print(f"size: {fp} : {size}kb")
            except OSError:
                continue

            if size > size_bytes:
                mb = round(size / (1024 * 1024), 1)
                print(f"[대용량] {fp} - {mb} MB")


if __name__ == '__main__':
    # base = Path.cwd() / "연습"
    base = Path(__file__).parent / "연습" # c:\bong\git\fs\rpa\p03_데스크탑\ch03_파일시스템관리\연습

    find_big_files(base, size_kb = 100)