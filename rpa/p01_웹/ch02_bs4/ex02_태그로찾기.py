# 데이터 추출
'''
1. HTML 태그로 추출
2. CSS 선택자로 추출 : id, class
3. HTML 속성으로 추출 : id, class, href, src, ...
4. 정규표현식으로 추출
5. XPath로 추출
6. Selenium으로 추출
7. API로 추출
8. Selenium 활용
9. BeautifulSoup으로 추출
10. Scrapy로 추출
'''
import bs4

html_example = """
<html>
    <body>
        <h1 id="title">나의 웹사이트</h1>
        <p>이것은 첫 번째 문단입니다.</p>
        <p>이것은 두 번째 문단입니다. 여기에는 <b>굵은 글씨</b>도 있습니다.</p>
        <div>
            <p>이것은 div 태그 안의 세 번째 문단입니다.</p>
        </div>
    </body>
</html>
"""

# HTLM 태그와 속성 또는 CSS 선택자(CSS Selector)를 사용하여 HTML안에서 모든 <p> 태그를 찾아 리스트 형태로 반환합니다.
# soup.select("태그명")
soup = bs4.BeautifulSoup(html_example, "html.parser") # html_example를 html.parser로 파싱
print(soup)
paragraph_elements = soup.select("p") # p 태그 찾기
print("찾은 개수:", len(paragraph_elements))

for e in paragraph_elements:
    print("\n23:", e) # 요수 출력
    print("24:",e.get_text()) # 태그 안의 내용만 출력 > 찾은 개수: 3
'''
23: <p>이것은 첫 번째 문단입니다.</p>
24: 이것은 첫 번째 문단입니다.

23: <p>이것은 두 번째 문단입니다. 여기에는 <b>굵은 글씨</b>도 있습니다.</p>
24: 이것은 두 번째 문단입니다. 여기에는 굵은 글씨도 있습니다.

23: <p>이것은 div 태그 안의 세 번째 문단입니다.</p>
24: 이것은 div 태그 안의 세 번째 문단입니다.
'''