import requests

target_url = "https://www.yna.co.kr/view/AKR20250923073400009?section=international/all" # 접근가능
# https://www.yna.co.kr/robots.txt로 했을 때 allow로 되어 있음
# target_url = "https://ko.wikipedia.org/wiki/한글" # 접근금지

try:
    response = requests.get(target_url)
    response.raise_for_status()
except requests.exceptions.HTTPError as e:
    print("페이지 로딩 에러:", e)
else:
    print("페이지 로딩 성공:", response.status_code)
    html_code = response.text

    print("전체 코드 길이:", len(html_code))
    print("----------------코드 미리 보기----------------")
    print(html_code[:2000])

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_code, 'html.parser')
title = soup.find('title').get_text()
print("추출된 제목:", title)