'''
browser.window.handles[0],[1]
browser.current_window_handle
browser.switch_to.window(핸들번호)
browser.close(): 현재 윈도우 닫기
'''
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("https://www.google.com")
print(f"첫 번째 탭 제목: {browser.title}")
time.sleep(2)

browser.execute_script("window.open('about:blank','_blank');")

all_tabs = browser.window_handles
print(f"탭 개수: {len(all_tabs)}")
print(f"탭: {all_tabs}")

browser.switch_to.window(all_tabs[1])
browser.get("https://www.python.org")
print(f"두 번째 탭의 현재 제목: {browser.title}")

time.sleep(2)

browser.switch_to.window(all_tabs[0])
print("첫 번째 탭으로 다시 전환했습니다.")
print(f"첫 번째 탭의 현재 제목: {browser.title}")

time.sleep(2)
browser.close() # 현재 윈도우 닫기

time.sleep(3)
browser.quit() # 전체 윈도우 닫기