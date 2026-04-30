from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, bs4

URL = "https://tech.kakao.com/blog"

browser = webdriver.Chrome()
browser.get(URL)

time.sleep(3)

post_titles = []

# 크롤링 루프 : 데이터가 충분히 쌓일 때까지 브라우저를 조작하고 수집하는 과정을 무한 반복
while len(post_titles) < 20:

    '''
        이 코드는 Selenium이 "화면에 데이터가 나타날 때까지 기다려라"라고 명령하는 부분입니다.

        ul.list_post: 클래스 이름(class)이 list_post인 <ul> 태그를 찾습니다.

        > (자식 결합자): 바로 아래 단계에 있는 직계 자식만 찾겠다는 뜻입니다.

        li: 그 자식들 중 <li> 태그를 찾습니다.

        정리하자면: "클래스가 list_post인 리스트(ul) 바로 밑에 있는 항목(li)이 나타날 때까지 기다려!"라는 뜻입니다. 리스트의 틀이 잡혔는지 확인하는 용도죠.
    '''
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'ul.list_post > li')))

    soup = bs4.BeautifulSoup(browser.page_source, 'html.parser')

    # list Comprehension(컴프리헨션)
    # 시퀀스(반복가능객체): 리스트, 튜플, 문자열, range()
    '''
        [표현식 for 항목 in 시퀀스 [if 조건문]]
        a = [1,2,3,4]
        result = [num * 3 for num in a]
        print(result) # [3, 6, 9, 12]
    '''
    # 데이터 중복 제거 : 한 줄의 코드로 현재 페이지의 모든 제목을 리스트로 만듭니다.
    current_titles = [tag.get_text(strip=True) for tag in soup.select("ul.list_post > li h4.tit_post")]
    '''
        이 코드는 BeautifulSoup을 통해 실제 "글 제목" 텍스트만 콕 집어서 가져오는 부분입니다.

        ul.list_post > li: 위와 동일하게 리스트의 각 항목(게시글 한 칸)을 가리킵니다.

        (공백, 후손 결합자): 가장 중요한 부분입니다! li 태그 안에 포함된 모든 하위 요소 중에서 찾으라는 뜻입니다. (직계 자식이 아니어도 상관없습니다.)

        h4.tit_post: 클래스 이름이 tit_post인 <h4> 태그를 찾습니다.

        정리하자면: "게시글 항목(li) 안 어딘가에 깊숙이 숨어있는 제목(h4.tit_post) 태그들을 전부 다 선택해줘!"라는 뜻입니다.
    '''

    # 새로운 제목만 추가
    new_titles_added = False
    for title in current_titles:
        if title not in post_titles:
            post_titles.append(title)
            new_titles_added = True

    # 새로 추가된 게 없거나 이미 20개 이상이면 종료
    if not new_titles_added or len(post_titles) >= 20:
        break

    # "다음 페이지" 버튼 클릭
    try:
        next_button = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.btn_next'))
        )
        next_button.click()
        print("'다음 페이지' 버튼 클릭 -> 새로운 게시물 로딩 대기...")
        time.sleep(2)
    except Exception:
        print("'다음 페이지' 버튼 없음, 마지막 페이지에 도달했습니다.")
        break

time.sleep(5)

# 브라우저 종료
browser.quit()

# 최종 결과 출력
print("\n--- 수집된 최신 게시물 제목 (상위 20개) ---")
for i, title in enumerate(post_titles[:20], start=1):
    print(f"{i}. {title}")
'''
--- 수집된 최신 게시물 제목 (상위 20개) ---
1. 카카오톡 예약하기에서 그려 본 캘린더
2. 카나나 스칼라 1회 세미나 현장 스케치
3. 수억 건의 보안 신호 속 진짜 위협 찾기 — AI로 보안 모니터링의 패러다임을 바꾸다
4. 학생에서 개발자로: 로또 구현부터 레거시 개선까지, 서버의 흐름을 배우다
5. 학생에서 개발자로: DB, 보안부터 AI까지, 정답보다 합리적인 선택을 배우다
6. 한국 문화 이해부터 화면 조작까지: Kanana-V 기능 확장의 모든 것
7. 2026 카카오그룹 신입크루 공채 코딩테스트 2차 문제해설
8. 2026 카카오그룹 신입크루 공채 코딩테스트 1차 문제해설
9. Kanana-o 신규 모델 및 API 베타 서비스를 공개합니다.
10. 잃어버린 리포트를 찾아서: 카카오 메시징 시스템의 경쟁 조건 문제와 안티 패턴 제거 과정
11. 카카오 AI 앰배서더 ‘KANANA 429 앰배서더’를 신규 모집합니다.
12. Kanana-2 개발기 (2): 개선된 post-training recipe를 중심으로
13. Kanana-2 개발기 (1): Pre-training에서의 의사결정들을 중심으로
14. “생각하고 답변하는” 카카오의 하이브리드 멀티모달 언어모델, Kanana-v-4b-hybrid 개발기
15. 초경량 클래식 형태소 분석기 개발기
16. 더 똑똑하고 효율적인 Kanana-2 오픈소스 공개
17. MongoDB 8.0 업그레이드 해야하는 12가지 이유
18. 더욱 똑똑하게 답하며, 더욱 풍부한 감정표현을 향한 Kanana-o의 진화 과정
19. ​한국어와 이미지를 한 번에, 카카오의 멀티모달 임베딩 모델 개발기
20. AI TOP 100이 우리에게 남긴 것들
'''