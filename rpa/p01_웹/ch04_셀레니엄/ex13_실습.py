from selenium import webdriver
from selenium.webdriver.chrome.options import Options # 옵션 설정을 위해 추가
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, bs4

URL = "https://www.youtube.com/results?search_query=자기전에+듣기+좋은+노래&sp=CAM%253D"

# --- 옵션 설정 ---
chrome_options = Options()
# 자동화 제어 메시지 제거 및 봇 감지 우회
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option("useAutomationExtension", False)
# 일반 브라우저처럼 보이게 유저 에이전트 설정
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36")

browser = webdriver.Chrome(options=chrome_options) # 옵션 적용
# ----------------

try:
    browser.get(URL)

    # 페이지가 완전히 로딩될 때까지 넉넉하게 대기
    time.sleep(5)

    post_titles = []

    while len(post_titles) < 20:

        WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'h3.title-and-badge #video-title')))

        soup = bs4.BeautifulSoup(browser.page_source, 'html.parser')
        current_titles = [tag.get_text(strip=True) for tag in soup.select("h3.title-and-badge #video-title")]

        new_titles_added = False
        for title in current_titles:
            if title and title not in post_titles:
                post_titles.append(title)
                print(f"수집 중: {title}")
                new_titles_added = True
            if len(post_titles) >= 20:
                break

        # 유튜브는 스크롤을 내려야 새로운 데이터가 로딩됩니다.
        if len(post_titles) < 20:
            browser.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
            time.sleep(2) # 스크롤 후 로딩 대기

        if not new_titles_added or len(post_titles) >= 20:
            break

except Exception as e:
    print(f"에러 발생: {e}")

finally:
    time.sleep(3)
    browser.quit()

# 최종 결과 출력
print("\n--- 수집된 최신 게시물 제목 (상위 20개) ---")
for i, title in enumerate(post_titles[:20], start=1):
    print(f"{i}. {title}")