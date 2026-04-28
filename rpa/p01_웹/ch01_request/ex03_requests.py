# 없을 경우 : 터미널에서 pip install requests
# 재 설치하려면 기존 삭제 : pip uninstall requests
import requests

# 정상 페이지 -> 페이지 있음
url_success = "https://www.python.org"

# 정상이 아닌 페이지 -> 페이지 없음
#url_fail = "https://www.python.org/this-page-does-not-exist"
#url_fail = "https://www.google.com/sea"
# 메가박스는 아래 코드가 정상 동작하지 않음!
url_fail = "https://www.megabox.co.kr/movie/011"

urls_to_check = [url_success, url_fail]

for url in urls_to_check:
    try: 
        response = requests.get(url)
        # 응답 상태가 200(성공)이 아닐 경우, Error
        print("response:",response)
        response.raise_for_status() # response: <Response [200]>, response: <Response [404]>
    except requests.exceptions.HTTPError as e:
        print("페이지 로딩 에러:", e)
    else:
        print("페이지 로딩 성공:", response.status_code)