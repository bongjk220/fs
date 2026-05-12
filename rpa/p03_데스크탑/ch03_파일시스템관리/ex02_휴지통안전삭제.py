# 휴지통으로 안전 삭제
'''
send2trash.send2trash(path)
'''
from pathlib import Path

def prepare_demo(base:Path):
    d = base / "연습" / "trash"
    d.mkdir(parents=True, exist_ok=True)

    for name in ["리포트.pdf", "메모.txt"]:
        (d / name).write_text("샘플", encoding="utf-8")

    return [d / "리포트.pdf", d / "메모.txt"]

def safe_trash(files, really:bool):
    try:
        import send2trash
    except ImportError:
        print("[안내] send2trash 미설치 : pip install send2trash")
        return
    
    for f in files:
        if really:
            send2trash.send2trash(f)
            print(f"[휴지통 보내기] {f}")
        else:
            print(f"[드라이런] 휴지통 예정 : {f}")

if __name__ == "__main__":
    # base = Path.cwd()
    base = Path(__file__).parent # c:\bong\git\fs\rpa\p03_데스크탑\ch03_파일시스템관리
    targets = prepare_demo(base)
    print(targets)

    safe_trash(targets, really=False)

    yn = input("해당 파일을 지울까요? y(es)/n(o) >")
    if yn.lower() == "y":
        safe_trash(targets, really=True)
