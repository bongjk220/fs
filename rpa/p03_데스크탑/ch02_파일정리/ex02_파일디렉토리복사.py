# shutil.copy(src, dst) : 보이는 부분만 복제
# shutil.copytree(src, dst) : 하위까지 복제
import shutil # 쉘유틸
from pathlib import Path

def copy_file_example(base:Path):
    src_file = base / "spam" / "file1.txt"

    # 디렉토리에 복사 (dst => 디렉토리)
    # shutil.copy(src, dst) : src는 파일, dst는 디렉토리
    copied1 = shutil.copy(src_file, base)
    print("결과:", copied1) # 결과: c:\bong\git\fs\rpa\p03_데스크탑\ch02_파일정리\연습\file1.txt

    # 파일명 지정 복사
    copied2 = shutil.copyfile(src_file, base / "spam" / "file5.txt")
    print("결과:", copied2) # 결과: c:\bong\git\fs\rpa\p03_데스크탑\ch02_파일정리\연습\spam\file5.txt


def copy_tree_example(base:Path):
    # spam 디렉토리 전체를 spam_backup으로 복사
    dst = base / "spam_backup"

    # 존재하면 디렉토리 제거
    if dst.exists():
        shutil.rmtree(dst)

    # 트리 복사
    copied_tree = shutil.copytree(base / "spam", dst)
    print("copy tree 결과:", copied_tree) # copy tree 결과: c:\bong\git\fs\rpa\p03_데스크탑\ch02_파일정리\연습\spam_backup


if __name__ == "__main__":
    # base = Path.cwd() / "연습"
    base = Path(__file__).parent / "연습" # c:\bong\git\fs\rpa\p03_데스크탑\ch02_파일정리\연습

    copy_file_example(base)

    copy_tree_example(base)