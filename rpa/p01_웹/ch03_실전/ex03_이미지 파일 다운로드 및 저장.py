# 이미지 파일 다운로드 및 저장
'''
wb
iter_content()
파일명: husband_and_wife.png
os.path.basename("url") -> xxx.png
os.path.join(디렉토리, 파일명)
'''
import requests, os

image_url = "//imgs.xkcd.com/comics/piercing.png"
#image_url = "//imgs.xkcd.com/comics/soniferous_aether.png"

if not image_url.startswith("http"):
    image_url = "https:" + image_url

try:
    # 현재 실행 중인 .py 파일의 절대 경로를 가져옵니다.
    current_file_path = os.path.abspath(__file__)
    print(current_file_path)
    # 그 파일이 들어있는 '폴더' 경로만 추출합니다.
    current_dir = os.path.dirname(current_file_path)
    print(current_dir)

    save_folder = os.path.join(current_dir, "img")
    print(save_folder)
    
    # 저장 폴더 생성
    os.makedirs(save_folder, exist_ok=True)

    response = requests.get(image_url, timeout=10)
    response.raise_for_status()

    file_name = os.path.basename(image_url) #piercing.png soniferous_aether.png
    save_path = os.path.join(save_folder, file_name)
    print(save_path)

    with open(save_path, "wb") as image_file:
        for chunk in response.iter_content(chunk_size=100000):
            if chunk:
                image_file.write(chunk)
    
    print("이미지 저장 성공", file_name)

except Exception as e:
    print("에러:", e)