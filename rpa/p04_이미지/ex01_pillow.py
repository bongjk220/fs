# pip install Pillow
from PIL import Image
from pathlib import Path

cur_dir = Path(__file__).parent
path = cur_dir / "사진.jpg"

im = Image.open(path)

print("파일명:", im.filename)
print("형식:", im.format) # 형식: JPEG

if hasattr(im, "format_description"):
    print("형식 설명:", im.format_description) # 형식 설명: JPEG (ISO 10918)
else:
    print("형식 설명 없음!")

w, h = im.size
print(f"크기:{w}픽셀 x {h}픽셀") # 크기:640픽셀 x 333픽셀

im.save(cur_dir /"사진_복사본.png")