import os
from pathlib import Path

def make_sample(root: Path):
    (root / 'spam').mkdir(parents=True, exist_ok=True)
    (root / 'spam' / "eggs").mkdir(parents=True, exist_ok=True)
    (root / 'spam' / "eggs" / "bacon").mkdir(parents=True, exist_ok=True)
    (root / 'spam' / "eggs2").mkdir(parents=True, exist_ok=True)

    for f in ["spam/file1.txt", "spam/file2.txt", "spam/eggs/file3.txt", "spam/eggs/bacon/file4.txt"]:
        (root / f).write_text("Hello", encoding="utf-8")

def show_list_str(root:Path):
    # 첫번째 방법 (old방법) os.listdir -> 문자열 목록
    full_path = str(root / "spam") # 경로를 인식하지 못하므로 str로 변환
    print(f"{full_path} 목록 :") # c:\bong\git\fs\rpa\p03_데스크탑\ch02_파일정리\연습\spam 목록 : 
    for p in os.listdir(full_path):
        print(p)
        '''
        eggs
        eggs2
        file1.txt
        file2.txt
        '''

def show_list_path(root:Path):
    # 두번째 방법 (new방법) Path.iterdir -> 경로포함 목록
    full_path = root / "spam"
    print(full_path.iterdir()) # <map object at 0x000001F71FE1F9A0>

    for p in full_path.iterdir():
        if p.is_dir():
            print(f"[{p}]")
        else:
            print(f"{p}")
        '''
        [c:\bong\git\fs\rpa\p03_데스크탑\ch02_파일정리\연습\spam\eggs]
        [c:\bong\git\fs\rpa\p03_데스크탑\ch02_파일정리\연습\spam\eggs2]
        c:\bong\git\fs\rpa\p03_데스크탑\ch02_파일정리\연습\spam\file1.txt
        c:\bong\git\fs\rpa\p03_데스크탑\ch02_파일정리\연습\spam\file2.txt
        '''

# if __name__ == "__main__":
# - "이 파일이 직접 실행된 것인지 , 아니면 다른 파일에 의해 불려와진(import된) 것인지"를 구분하는 역할"을 합니다. __main__
# __name__ : 현재 실행 중인 모듈(파일)의 이름
if __name__ == "__main__":
    # base = Path.cwd() / "연습"
    base = Path(__file__).parent / "연습" # c:\bong\git\fs\rpa\p03_데스크탑\ch02_파일정리\연습

    make_sample(base)
    show_list_str(base)
    show_list_path(base)