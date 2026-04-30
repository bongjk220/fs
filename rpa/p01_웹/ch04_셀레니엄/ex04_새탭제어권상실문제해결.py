'''
click()
'''
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("https://www.naver.com")

time.sleep(1)

try:
    news_link = browser.find_element(By.LINK_TEXT, '뉴스')  
    news_link.click()

    time.sleep(3)

    # 모든 창(탭)의 핸들러를 가져옴
    all_windows = browser.window_handles

    # 마지막으로 열린 창(새 탭)으로 제어권을 전환
    browser.switch_to.window(all_windows[-1]) # 0으로 했을때는 첫번째 탭, -1은 마지막 탭

    print("title:", browser.title) # title: 네이버 뉴스
    print("current_url:", browser.current_url) # current_url: https://news.naver.com/
    # print("page_source:", browser.page_source)

except Exception as e:
    print("에러:",e)

time.sleep(10)
browser.quit()