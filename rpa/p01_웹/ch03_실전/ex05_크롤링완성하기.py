import requests, os, bs4, time

url = 'https://xkcd.com'

# 현재 실행 중인 .py 파일의 절대 경로를 가져옵니다.
current_file_path = os.path.abspath(__file__)
# 그 파일이 들어있는 '폴더' 경로만 추출합니다.
current_dir = os.path.dirname(current_file_path)
save_folder = os.path.join(current_dir, "img")
# 저장 폴더 생성
os.makedirs(save_folder, exist_ok=True) # os.makedirs('xkcd_comics', exist_ok=True)

cnt = 0

# URL이 '#'으로 끝나지 않는 동안 무한 반복 (1화까지 거슬러 올라감)
while not url.endswith("#"): # 1페이지가 "#"
    cnt += 1
    if cnt > 10:
        print("설정한 수집 개수(10개)에 도달하여 루프를 중단합니다.")
        break

    print("-----------", cnt ,"-----------")

    try:
        # 1. 페이지 정보 가져오기
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = bs4.BeautifulSoup(response.text, "html.parser")

        # 2. 만화 이미지 태그 찾기 (#comic ID 내부의 img 태그)
        comic_image_element = soup.select("#comic img")

        if comic_image_element:
            # 이미지 소스(src) 추출
            image_url = comic_image_element[0].get("src")

            # 상대 경로(//로 시작)일 경우 프로토콜(https:) 추가
            if not image_url.startswith("http"):
                image_url = "https:" + image_url

            # 3. 이미지 실제 데이터 요청
            response_img = requests.get(image_url, timeout=10)
            response_img.raise_for_status()

            # 4. 저장 경로 설정 (폴더명 + 파일명)
            save_path = os.path.join(save_folder, os.path.basename(image_url))

            # 5. 바이너리 쓰기 모드로 파일 저장 (메모리 절약을 위해 chunk 단위 실행)
            with open(save_path, "wb") as image_file:
                for chunk in response_img.iter_content(100000):
                    if chunk: # 빈 청크 방지
                        image_file.write(chunk)
            print(f"저장 완료: {save_path}")
        
        else:
            print("만화 이미지를 찾지 못했습니다.")

        # 6. '이전(Prev)' 버튼 링크 찾기
        prev_link_element = soup.select('a[rel="prev"]')
        if not prev_link_element:
            print("이전 페이지가 없어 크롤링을 종료합니다.")
            break

        # 다음 루프에서 방문할 URL 갱신
        prev_page_path = prev_link_element[0].get("href")

        # URL이 상대 경로인지 절대 경로인지 체크하여 결합
        if not prev_page_path.startswith("http"):
            url = "https://xkcd.com" + prev_page_path
        else:
            url = prev_page_path
 
        print("   다음에 방문할 주소:", url)

    except Exception as e:
        print("에러:", e)

    # [매너] 서버 부하를 줄이기 위한 2초 대기
    time.sleep(2)

# 루프 종료 후 최종 확인 메시지
print("====================================")
print("모든 크롤링 작업이 안전하게 종료되었습니다.")
print("====================================")