# selenium + beautifulsoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import bs4, time

# 셀레늄의 역할
browser = webdriver.Chrome()
browser.get("https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=105")

time.sleep(3)

html_source = browser.page_source
# 뷰티풀숩의 역할
soup = bs4.BeautifulSoup(html_source, "html.parser")

# div.sa_item_flex a.sa_text_title
# -> div 태그 중에서 클래스명이 sa_item_flex 이고
# -> 그 자손 중 a 태그 이면서 클래스명이 sa_text_title
headlne_links = soup.select("div.sa_item_flex a.sa_text_title")

print("--- 네이버 IT/과학 헤드라인 뉴스 ---")
for link in headlne_links:
    title = link.get_text(strip=True) # strip=True -> 양쪽 공백 자동 제거
    print(f"- {title}")

time.sleep(30)
browser.quit()