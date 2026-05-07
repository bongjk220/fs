# os.walk()
import os, shutil
from pathlib import Path

def walk_report(base):
    root = base / "spam"

    # os.walk() : 폴더 트리를 순회하면서 폴더, 하위폴더, 파일 정보를 튜플로 반환
    for folder_name, subfolders, files in os.walk(root):
        print("[폴더]", folder_name)

        for sf in subfolders:
            print("    ┕[폴더]", sf)

        for f in files:
            print("    └[파일]", f)

    '''
    [폴더] c:\bong\git\fs\rpa\p03_데스크탑\ch02_파일정리\연습\spam\eggs
        ┕[폴더] bacon
        └[파일] file3.txt
    [폴더] c:\bong\git\fs\rpa\p03_데스크탑\ch02_파일정리\연습\spam\eggs\bacon
        └[파일] file4.txt
    [폴더] c:\bong\git\fs\rpa\p03_데스크탑\ch02_파일정리\연습\spam\eggs2
    '''

def rename_uppercase(base):
    root = base / "spam"

    # os.walk() : 폴더 트리를 순회하면서 폴더, 하위폴더, 파일 정보를 튜플로 반환
    for folder_name, subfolders, files in os.walk(root):
        p = Path(folder_name)
        for f in files:
            src = p / f
            dst = p / f.upper()

            if src.name != dst.name:
                shutil.move(src, dst) # move() 이름 변경
    

if __name__ == "__main__":
    # base = Path.cwd() / "연습"
    base = Path(__file__).parent / "연습" # c:\bong\git\fs\rpa\p03_데스크탑\ch02_파일정리\연습
    print("-" * 80)

    # walk_report(base)

    rename_uppercase(base)