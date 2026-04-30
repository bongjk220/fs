# 웹 페이지의 특정 요소 찾기
'''
find_element(): 하나 찾기, 없으면 에러
find_elements(): 여러 개 찾기, 없으면 빈 리스트

검색 기준
    id -> By.ID
    class -> By.CLASS_NAME
    tag -> By.TAG_NAME
    name -> By.NAME
    css -> By.CSS_SELECTOR
    By.LINK_TEXT
    XPATH -> By.XPATH

    예) ele = browser.find_element(By.ID, 'id값')
'''
''' By 클릭시 찾기
    ID: ByType = "id"
    XPATH: ByType = "xpath"
    LINK_TEXT: ByType = "link text"
    PARTIAL_LINK_TEXT: ByType = "partial link text"
    NAME: ByType = "name"
    TAG_NAME: ByType = "tag name"
    CLASS_NAME: ByType = "class name"
    CSS_SELECTOR: ByType = "css selector"
'''

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("https://www.naver.com")

time.sleep(2)

try:
    # find_element(하나찾기, 없으면 에러(try~except)) : bs4의 select_one()에 해당
    search_box = browser.find_element(By.ID, 'query')
    print(search_box.tag_name) # input

    # search_box.send_keys("파이썬")
    # search_box.submit()
    # time.sleep(2)

except Exception as e:
    print("에러: ", e)

print('-'*50)

# find_elements(여러개찾기, 없으면 빈 리스트) : bs4의 select()에 해당
menu_links = browser.find_elements(By.CLASS_NAME, 'link_service')
print(len(menu_links)) # 11

for link in menu_links:
    if link.text.strip():
        print("링크 :", link.text.strip())
'''
링크 : 메일
링크 : 카페
링크 : 블로그
링크 : 스토어
링크 : 뉴스
링크 : 증권
링크 : 부동산
링크 : 지도
링크 : 웹툰
링크 : 치지직
추천
링크 : 바로가기 펼침
'''

time.sleep(5)
browser.quit()