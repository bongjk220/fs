# pip install bs4
import requests
import bs4 # BeautifulSoup은 요청은 못해서 requests를 먼저 불러온다.

target_url = "https://news.naver.com/section/105"
# target_url = "https://news.naver.com/section/999" # 에러: 500 Server Error: Internal Server Error for url: https://news.naver.com/section/999

try:
    response = requests.get(target_url)
    response.raise_for_status() # 강제 에러 발생(상태값이 200이 아니면)
    print(response) # <Response [200]>
    soup = bs4.BeautifulSoup(response.text, "html.parser")

    print(type(soup)) # <class 'bs4.BeautifulSoup'>
    print(soup.title) # <title>IT/과학 : 네이버 뉴스</title>
    print(soup.title.string) # IT/과학 : 네이버 뉴스
    print(soup.find_all('h2'))
    print('-'*100)

    # 뉴스 제목을 담고 있는 태그를 찾아 출력 (네이버 뉴스 구조에 따라 다를 수 있음)
    titles = soup.select(".sa_text_strong") # 뉴스 제목 클래스 선택
    for title in titles:
        print(title.get_text())

except requests.exceptions.HTTPError as e:
    print("에러:", e)
else:
    print("페이지 로딩 성공:", response.status_code) # 페이지 로딩 성공: 200