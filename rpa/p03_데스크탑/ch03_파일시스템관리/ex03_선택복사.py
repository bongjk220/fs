'''
os.walk
shutil.copy
'''
import os, shutil
from pathlib import Path

def selective_copy(src: Path, out: Path, exts: tuple[str, ...]):
    out.mkdir(parents=True, exist_ok=True)

    for folder, _, files in os.walk(src):
        p = Path(folder) # ./연습/자료원본

        for name in files:
            if Path(name).suffix.lower() in exts:
                src = p / name
                dst = out / name # ./연습/모아두기/?.pdf
                
                # test.pdf -> test_1.pdf -> test_2.pdf ...
                n = 1
                temp_file_name = dst.stem
                while dst.exists():
                    dst = out / f"{temp_file_name}_{n}{dst.suffix}"
                    n += 1

                shutil.copy(src, dst)
                print(f"[복사] {src} -> {dst.name}")



if __name__ == "__main__":
    # base = Path.cwd() / "연습"
    base = Path(__file__).parent / "연습" # c:\bong\git\fs\rpa\p03_데스크탑\ch03_파일시스템관리\연습
    src = base / "자료원본"
    out = base / "모아두기"

    selective_copy(src, out, (".pdf", ".jpg"))