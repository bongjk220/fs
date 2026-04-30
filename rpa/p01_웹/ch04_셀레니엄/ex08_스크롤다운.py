import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get("https://www.naver.com")

time.sleep(2)

try:
    search_box = browser.find_element(By.ID, 'query')
    search_keyword = "생성형 AI"
    search_box.send_keys(search_keyword)
    time.sleep(0.2) # [매너] 천천히 하도록
    search_box.send_keys(Keys.ENTER)
    time.sleep(2) # 

    # 페이지 전체 선택, 스크롤 다운
    html_body = browser.find_element(By.TAG_NAME, 'html')

    # html_body.send_keys(Keys.PAGE_DOWN)
    # time.sleep(2)
    # html_body.send_keys(Keys.PAGE_DOWN)
    # time.sleep(2)
    # html_body.send_keys(Keys.PAGE_DOWN)
    # time.sleep(2)
    # html_body.send_keys(Keys.PAGE_DOWN)
    # time.sleep(2)
    # html_body.send_keys(Keys.PAGE_DOWN)
    a = 0
    while a < 10:
        html_body.send_keys(Keys.PAGE_DOWN)
        time.sleep(2)
        a += 1

    print("스크롤 완료")

except Exception as e:
    print("에러:",e)

time.sleep(10)
browser.quit()