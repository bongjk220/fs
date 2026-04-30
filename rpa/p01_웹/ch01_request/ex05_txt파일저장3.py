# import requests
# import os
import requests, os

target_url = "https://www.gutenberg.org/files/57362/57362-0.txt"

try:
    response = requests.get(target_url)
    response.raise_for_status()
    print("요청한 응답 정보는?", response) # <Response [200]>
    print("요청한 응답 코드는?", response.status_code) # 200
    print("요청한 응답 헤더는?", response.headers)
    # print("요청한 응답 텍스트는?", response.text)

    # 현재 실행 중인 .py 파일의 절대 경로를 가져옵니다.
    current_file_path = os.path.abspath(__file__)
    print(current_file_path)
    # 그 파일이 들어있는 '폴더' 경로만 추출합니다.
    current_dir = os.path.join(os.path.dirname(current_file_path), "../../")
    print(current_dir)

    # 만약 해당 폴더가 없다면 자동으로 생성해주는 코드 (안전장치)
    if not os.path.exists(current_dir):
        os.makedirs(current_dir)

    # 폴더 경로와 파일 이름을 합쳐줍니다.
    save_path = os.path.join(current_dir, "윤동주_시.txt")
    print(save_path)


    cnt = 0
    # 윤동주_시.txt -> 387KB
    with open(save_path, "wb") as my_file:
        # chunk_size=100000 Byte -> 약 100KB
        for chunk in response.iter_content(chunk_size=100000):
            cnt += 1
            print(cnt)
            my_file.write(chunk)

except requests.exceptions.HTTPError as e:
    print("페이지 로딩 에러:", e)
else:
    print("페이지 로딩 성공:", response.status_code)