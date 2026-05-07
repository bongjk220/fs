# zip 파일 만들기
'''
zipfile.ZipFile('spam.zip', 'w').write('spam.txt')
compresslevel : 압축율 (1-9, 9가 가장 높은 압축율) - 압축율이 높을수록 압축하는데 시간이 오래 걸림 6정도가 적당
'''
import zipfile
from pathlib import Path

def make_text(base:Path):
    # 압축 대상 파일 만들기
    f = base / "spam" / "file_zip_demo.txt"
    f.write_text("Hello" * 1000000, encoding="utf-8")
    return f

def write_zip(file_path:Path):
    zip_path = file_path.parent / "example.zip"

    with zipfile.ZipFile(zip_path, "w") as z:
        z.write(file_path, compress_type=zipfile.ZIP_DEFLATED, compresslevel=6)

    print("zip 생성 완료", zip_path) # zip 생성 완료 c:\bong\git\fs\rpa\p03_데스크탑\ch02_파일정리\연습\spam\example.zip

if __name__ == '__main__':
    # base = Path.cwd() / "연습"
    base = Path(__file__).parent / "연습" # c:\bong\git\fs\rpa\p03_데스크탑\ch02_파일정리\연습

    target = make_text(base)
    print(target) # c:\bong\git\fs\rpa\p03_데스크탑\ch02_파일정리\연습\spam\file_zip_demo.txt

    write_zip(target)