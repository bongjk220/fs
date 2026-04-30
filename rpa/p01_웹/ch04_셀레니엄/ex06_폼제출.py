# 폼 제출하고 결과 확인하기
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get("https://www.naver.com")

time.sleep(2)

try:
    search_box = browser.find_element(By.ID, 'query')
    search_keyword = "오늘 날씨"
    search_box.send_keys(search_keyword)
    # search_box.send_keys(Keys.BACKSPACE)
    search_box.send_keys(Keys.ENTER)
    # search_box.submit()

except Exception as e:
    print("에러:",e)

time.sleep(10)
browser.quit()