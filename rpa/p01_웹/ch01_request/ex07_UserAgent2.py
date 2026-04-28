import requests

# 1. 브라우저 정보를 담은 헤더 설정 (크롬 브라우저 예시)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

url_success = "https://www.python.org"
url_fail = "https://www.megabox.co.kr/movie/011"

urls_to_check = [url_success, url_fail]

for url in urls_to_check:
    try: 
        # 2. 요청 시 headers를 함께 보냄
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
    except requests.exceptions.HTTPError as e:
        print(f"[{url}] HTTP 에러 발생:", e)
    except requests.exceptions.ConnectionError as e:
        print(f"[{url}] 연결 에러 발생 (차단됨):", e)
    except Exception as e:
        print(f"[{url}] 기타 에러:", e)
    else:
        print(f"[{url}] 페이지 로딩 성공:", response.status_code)