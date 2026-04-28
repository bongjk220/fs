import bs4

html_example = """
<html>
    <header id="header">
        <nav>
            <ul>
                <li><a href="https://www.naver.com">네이버</a></li>
                <li><a href="https://www.google.com">구글</a></li>
                <li><a href="https://www.daum.net">다음</a></li>
            </ul>
        </nav>
    </header>
    <body>
        <h1 id="header">오늘의 메뉴</h1>
        <ul>
            <li class="menu-item">김치찌개</li>
            <li class="menu-item">된장찌개 (추천)</li>
            <li class="menu-item">비빔밥</li>
            <li class="side-dish">계란찜</li>
        </ul>
    </body>
</html>
"""

soup = bs4.BeautifulSoup(html_example, "html.parser")

menu_items = soup.select(".menu-item") # class가 menu-item 가져옴
# menu_items = soup.select("li") # class가 li 전부 가져옴
# menu_items = soup.select("body li") # class가 body의 li만 가져옴
# menu_items = soup.select("#header") # id가 header의 전부 가져옴



for item in menu_items:
    print(item.get_text())
'''
김치찌개
된장찌개 (추천)
비빔밥
'''

for item in menu_items:
    text = item.get_text()
    if "(추천)" in text:
        print(f"⭐ 오늘 점심은 이거다! -> {text}")
    else:
        print(text)
'''
김치찌개
⭐ 오늘 점심은 이거다! -> 된장찌개 (추천)
비빔밥'''