import bs4

html_example = """
<html>
    <body>
        <h1>유용한 링크 모음</h1>
        <a id="site1" href="https://www.google.com">구글</a>
        <a id="site2" href="https://www.naver.com">네이버</a>
        <a id="site3" href="/ko/docs/python">파이썬 내부 문서 링크</a>
        <p>위 링크들은 매우 유용합니다</p>
    </body>
</html>
"""

soup = bs4.BeautifulSoup(html_example, "html.parser")

# 링크 태그만 검색
link_tags = soup.select("a")

print("목록 추출")
for link in link_tags:
    #print("\n",link.get_text())
    #print(link.get("href"))

    # .get("속성명")는 태그 내부의 작성된 특정 속성의 값을 가져옵니다. 
    print(f'텍스트:{link.getText()}, url:{link.get("href")}') # 태그안 정보 getText로 해도 된다., href 속성명 가져옴
    # print(f"텍스트:{link.get_text()}, url:{link.get('href')}") # get_text로 해도 된다.
    # print(f'텍스트:{link.getText()}, url:{link.get("id")}') # Id 속성명 가져옴
'''
목록 추출

 구글
https://www.google.com
텍스트:구글, url:https://www.google.com

 네이버
https://www.naver.com
텍스트:네이버, url:https://www.naver.com

 파이썬 내부 문서 링크
/ko/docs/python
텍스트:파이썬 내부 문서 링크, url:/ko/docs/python
'''
