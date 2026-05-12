# '드라이런(Dry-run)' 패턴?
# 파일 삭제와 같은 위험한 작업을 수행하기 전에 미리 결과를 확인
# 프로그램을 실제로 실행하지 않고, 코드가 어떻게 동작하는지 한 줄씩 추적하는 방법
# Q: 이 코드를 Dry-run 해보세요?
# A: 위 문장의 의미는? 코드 실행 흐름을 한 줄씩 설명해보세요.
'''
os.unlink : 단일 파일을 삭제합니다. (본 예제에서 사용됨)
os.rmdir : 빈폴더 삭제, 폴더 안에 파일이 있으면 에러가 발생합니다.
shutil.rmtree : 폴더 전체, 내부 파일과 하위 폴더를 포함하여 통째로 삭제합니다. (주의 필요)
'''
import os
from pathlib import Path
from tkinter import Y

def prepare_demo(base:Path):
    d = base / "연습" / "dryrun"
    d.mkdir(parents=True, exist_ok=True)

    for name in ["note.rxt", "temp.rxt", "test.txt"]:
        (d / name).write_text("샘플", encoding="utf-8")

    return d

def find_targets(demo:Path, param:str):
    return list(demo.glob(param)) # glob 패턴으로 파일 찾기 : glob 패턴은 와일드카드(*, ?, [])를 사용하여 파일을 검색하는 방법입니다. 예를 들어, *.txt는 모든 .txt 파일을 찾습니다.

def delete_with_dry_run(files, really:bool):
    for f in files:
        if really:
            os.unlink(f)
            print(f"[삭제] {f}")
        else:
            print(f"[삭제 예정] {f}")

if __name__ == '__main__':
    # base = Path.cwd()
    base = Path(__file__).parent # c:\bong\git\fs\rpa\p03_데스크탑\ch03_파일시스템관리

    # dry-run 패턴을 위한 데모 파일 준비
    demo = prepare_demo(base)

    # 데모 파일 찾기
    targets = find_targets(demo, "*.rxt")
    print(targets)

    # 데모 파일 삭제
    delete_with_dry_run(targets, really=False)

    # 데모 파일 제거
    yn = input("해당 파일을 지울까요? y(es)/n(o) >")
    if yn.lower() == "y":
        delete_with_dry_run(targets, really=True)