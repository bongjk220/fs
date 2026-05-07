import zipfile
from pathlib import Path

def read_zip_info(zf:Path):
    with zipfile.ZipFile(zf) as z:
        names = z.namelist()

        print("[zip 내 목록]", names) # [zip 내 목록] ['bong/git/fs/rpa/p03_데스크탑/ch02_파일정리/연습/spam/file_zip_demo.txt']

        if names:
            info = z.getinfo(names[0])
            print(f"info: {info}") 
            # [zip 내 목록] ['bong/git/fs/rpa/p03_데스크탑/ch02_파일정리/연습/spam/file_zip_demo.txt'] info: <ZipInfo filename='bong/git/fs/rpa/p03_데스크탑/ch02_파일정리/연습/spam/file_zip_demo.txt' compress_type=deflate filemode='-rw-rw-rw-' file_size=5000000 compress_size=7305>
            ratio = round(info.file_size / max(1, info.compress_size), 2)
            print(f"원본: {info.file_size}B, 압축: {info.compress_size}B, 압축비율: {ratio}배 압축")
            # 원본: 5000000B, 압축: 7305B, 압축비율: 684.46배 압축


def extract_zip(zip_path:Path, out_dir:Path):
    out_dir.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(zip_path) as z:
        z.extractall(out_dir)
    print("[추출 완료]", out_dir) # [추출 완료] c:\bong\git\fs\rpa\p03_데스크탑\ch02_파일정리\연습\spam\unzipped


if __name__ == '__main__':
    # base = Path.cwd() / "연습" / "spam"
    base = Path(__file__).parent / "연습" / "spam" # c:\bong\git\fs\rpa\p03_데스크탑\ch02_파일정리\연습\spam
    zf = base / "example.zip"

    read_zip_info(zf)

    extract_zip(zf, base / "unzipped")