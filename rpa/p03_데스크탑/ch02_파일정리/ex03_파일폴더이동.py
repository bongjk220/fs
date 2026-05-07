import shutil
from pathlib import Path


def move_to_folder(base:Path):
    src = base / "spam" / "file1.txt"
    dst_folder = base / "spam2"
    dst_folder.mkdir(parents=True, exist_ok=True)

    # 폴더 이동
    new_path = shutil.move(src, dst_folder)
    print("[move-폴더] => ", new_path) # [move-폴더] => c:\bong\git\fs\rpa\p03_데스크탑\ch02_파일정리\연습\spam2\file1.txt


# 파일 이동 + 이름 변경
def move_to_rename(base:Path):
    #src = base / "spam" / "file2.txt"
    src = base / "spam2" / "new_name.txt"

    dst_path = base / "spam2" / "old_name.txt"
    new_path = shutil.move(src, dst_path)
    print("[move-rename] => ", new_path) # [move-rename] =>  c:\bong\git\fs\rpa\p03_데스크탑\ch02_파일정리\연습\spam2\new_name.txt


# 현재 파일이 실행 : __name__ = "__main__"
# 외부에서 현재 파일을 호출 : __name__ = "ex03_파일폴더이동"
if __name__ == "__main__":
    # base = Path.cwd() / "연습"
    base = Path(__file__).parent / "연습" # c:\bong\git\fs\rpa\p03_데스크탑\ch02_파일정리\연습

    # 파일이동
    # move_to_folder(base)

    # 파일 이름 바꾸기
    move_to_rename(base)