# 셀레니엄
# pip install selenium
'''
WebDriver
    Chrome -> webdriver.Chrome()
    Firefox -> webdriver.Firefox()
    Edge -> webdriver.Edge()
browser.get(url)
'''
import time
from selenium import webdriver

# browser = webdriver.Firefox() # 가상의 파이어폭스 브라우저를 열게 함
# browser = webdriver.Edge() # 가상의 엣지 브라우저를 열게 함
browser = webdriver.Chrome() # 가상의 크롬 브라우저를 열게 함

target_url = "https://www.python.org"
# target_url = "https://www.megabox.co.kr"
# target_url = "https://www.wikipedia.org"
# target_url = "https://www.naver.co.kr"
browser.get(target_url)

time.sleep(5) # 브라우저를 5초 동안 유지
browser.quit() # 브라우저 끄기 > 버전 올라가서 안써도 꺼짐