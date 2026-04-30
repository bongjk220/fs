'''
<div class="string-major" aria-label="We detect that your web browser is">
    <a href="/detect/what-version-of-chrome-do-i-have/">Chrome 147 on Windows 10</a>
</div>
'''
# 헤드리스 브라우저
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# 주석처리했다가 (화면보면서) 테스트 다 끝나면 주석 풀어서 사용
chrome_options = Options()
chrome_options.add_argument('--headless') # 헤드리스 모드 활성화
chrome_options.add_argument('--no-sandbox') # 일부 환경에서 권장되는 옵션
chrome_options.add_argument('--disable-dev-shm-usage') # 리소스 문제 방지용

browser = webdriver.Chrome(options=chrome_options)
browser.get("https://www.whatismybrowser.com")

print(f"현재 페이지 제목: {browser.title}")

try:
    detected_browser = browser.find_element(By.CSS_SELECTOR, '.string-major')
    print(f"감지된 브라우저 정보: {detected_browser.text}")
except Exception as e:
    print("에러:",e)

time.sleep(1)
browser.quit()
print("브라우저를 종료했습니다.")