import requests

# https://www.useragentstring.com/
# 1. 브라우저 정보를 담은 헤더 설정 (크롬 브라우저 예시)
headers = {
    "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36"
    )
}

url_success = "https://ko.wikipedia.org/wiki/"
url_fail = "https://www.megabox.co.kr"

urls_to_check = [url_success, url_fail]

for url in urls_to_check:
    try: 
        # 2. 요청 시 headers를 함께 보냄
        # response = requests.get(url)
        '''
            [https://ko.wikipedia.org/wiki/] HTTP 에러 발생: 403 Client Error: Forbidden for url: https://ko.wikipedia.org/wiki/
            [https://www.megabox.co.kr] 연결 에러 발생 (차단됨): ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))
        '''
        response = requests.get(url, headers=headers, timeout=10)
        '''
            [https://ko.wikipedia.org/wiki/] 페이지 로딩 성공: 200
            [https://www.megabox.co.kr] 페이지 로딩 성공: 200
        '''

        response.raise_for_status()
        
    except requests.exceptions.HTTPError as e:
        print(f"[{url}] HTTP 에러 발생:", e)
    except requests.exceptions.ConnectionError as e:
        print(f"[{url}] 연결 에러 발생 (차단됨):", e)
    except Exception as e:
        print(f"[{url}] 기타 에러:", e)
    else:
        print(f"[{url}] 페이지 로딩 성공:", response.status_code)