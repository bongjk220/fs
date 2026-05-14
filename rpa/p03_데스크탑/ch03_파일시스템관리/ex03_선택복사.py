'''
os.walk
shutil.copy
'''
import os, shutil
from pathlib import Path

def selective_copy(src: Path, out: Path, exts: tuple[str, ...]):

    # 연습/자료원본 폴더 생성 및 파일생성 --> 없어서 추가
    src.mkdir(parents=True, exist_ok=True)
    for name in ["test.pdf", "test.jpg", "데이터.xlsx"]:
        (src / name).write_text("샘플", encoding="utf-8")

    # 연습/모아두기 폴더 생성
    out.mkdir(parents=True, exist_ok=True)

    for folder, _, files in os.walk(src): # src 경로를 시작으로 모든 하위 폴더를 순회합니다.
        p = Path(folder) # ./연습/자료원본

        for name in files:
            if Path(name).suffix.lower() in exts: # 파일의 확장자를 추출하여 소문자로 바꿉니다 (예: .JPG -> .jpg).
                src = p / name # 실제 소스 파일 경로
                dst = out / name # 복사될 목적지 경로 =>./연습/모아두기/?.pdf
                
                n = 1
                temp_file_name = dst.stem # # 확장자를 제외한 파일 이름
                while dst.exists(): # 목적지 폴더에 같은 이름의 파일이 있는지 확인
                    # test.pdf -> test_1.pdf -> test_2.pdf ...
                    dst = out / f"{temp_file_name}_{n}{dst.suffix}"
                    n += 1

                shutil.copy(src, dst) # 최종적으로 결정된 경로로 파일을 복사
                print(f"[복사] {src} -> {dst.name}")



if __name__ == "__main__":
    # base = Path.cwd() / "연습"
    base = Path(__file__).parent / "연습" # c:\bong\git\fs\rpa\p03_데스크탑\ch03_파일시스템관리\연습
    src = base / "자료원본"
    out = base / "모아두기"

    selective_copy(src, out, (".pdf", ".jpg"))