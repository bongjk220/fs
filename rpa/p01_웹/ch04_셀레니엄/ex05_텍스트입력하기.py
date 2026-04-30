# 폼에 텍스트 입력하기
'''
.send_keys('입력할 텍스트')
<input type="text">
<input type="password">
<textarea>
'''

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("https://www.naver.com")
time.sleep(2)

try:
    search_box = browser.find_element(By.ID, 'query')
    search_keyword = "파이썬"
    search_box.send_keys(search_keyword)

    # 검색 버튼 클릭
    search_btn = browser.find_element(By.CLASS_NAME, 'btn_search')
    search_btn.click()
    # login_btn = browser.find_element(By.CLASS_NAME, 'MyView-module__link_login___HpHMW')
    # login_btn.click()

except Exception as e:
    print("에러:",e)


time.sleep(10)
browser.quit()