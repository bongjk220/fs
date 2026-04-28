import requests
from requests.exceptions import HTTPError, RequestException

def fetch_wikipedia_page(title):
    base_url = f"https://ko.wikipedia.org/wiki/"
    url = base_url + title

    # Wikipedia User-Agent 정책에 따라 고유한 User-Agent를 사용해야 한다.
    headers = {
        # User-Agent 헤더는 ASCII 문자만 사용해야 한다. 한글 설명은 주석으로 남긴다.
        # 아래 문자열은 "학습용 스크립트"와 "연락처"를 영어로 표현한 것이다.
        "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36"
        )
    }

    # HTTP 요청을 수행하고 오류를 처리한다.
    try: 
        # 서버가 응답을 주지 않고 무한정 버틸 때, 10초 뒤에 연결을 강제로 종료
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status() # HTTP 오류 시 예외 발생
        return response
    except HTTPError as http_err:
        # HTTP 403 등 상태 코드 오류 처리
        raise HTTPError(
            f"HTTP 오류가 발생했습니다: {http_err.response.status_code}"
        ) from http_err
    except RequestException as req_err:
        # 네트워크 연결 실패 또는 기타 요청 관리 오류           
        raise RequestException(
            "네트워크 문제 또는 연결 오류가 발생했습니다."
            "현재 실행 환경에서 인터넷 접근이 제한되어 있을 수 있습니다."
        ) from req_err


title = "한글"
try:
    response = fetch_wikipedia_page(title)

    cnt = 0
    with open("wiki_한글.html", "wb") as my_file:
        for chunk in response.iter_content(chunk_size=100000):
            cnt += 1
            print(cnt)
            my_file.write(chunk)

except HTTPError as http_error:
    print(http_error)
except RequestException as req_error:
    print(req_error)