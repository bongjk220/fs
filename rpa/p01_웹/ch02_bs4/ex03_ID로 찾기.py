import bs4

html_example = """
<html>
    <body>
        <div id="header">
            <h1>블로그 제목</h1>
        </div>
        <div id="content">
            <p>이것은 본문 내용입니다.</p>
            <p>스크래핑은 <b>재미있습니다.</b></p>
        </div>

        <div id="content">
            <p>이것은 두번째 본문 내용입니다.</p>
            <p>스크래핑은 <b>재미없습니다.</b></p>
        </div>
        <div id="footer">
            <p>Copyright 2026. All Rights Reserved.</p>
        </div>
    </body>
</html>
"""

soup = bs4.BeautifulSoup(html_example, "html.parser")

content_div = soup.select("#content")
print(type(content_div)) # <class 'bs4.element.ResultSet'>
print(content_div)
# print(content_div.get_text()) # AttributeError

if content_div:
    for ele in content_div:
        print(ele.get_text())
else:
    print("없음")

# select_one은 리스트가 아닌 '객체 하나'를 바로 돌려줍니다.
content_div = soup.select_one("#content")
print(content_div)

if content_div:
    print(content_div.get_text()) # 반복문 없이 바로 사용 가능

print('-' * 60)

html_example = """
<html>
    <body>
        <div id="header">
            <h1>블로그 제목</h1>
        </div>
        <div id="content">
            <p>이것은 본문 내용입니다.</p>
            <p>스크래핑은 <b>재미있습니다.</b></p>
        </div>
        <div id="footer">
            <p>Copyright 2026. All Rights Reserved.</p>
        </div>
    </body>
</html>
"""

soup = bs4.BeautifulSoup(html_example, "html.parser")

# select_one은 리스트가 아닌 '객체 하나'를 바로 돌려줍니다.
content_div = soup.select_one("#content")
print(type(content_div)) # <class 'bs4.element.Tag'>
print(content_div)

if content_div:
    print(content_div.get_text()) # 반복문 없이 바로 사용 가능

print("-" * 20)

# content_div 있으면 True 없으면 False
if content_div:
    for ele in content_div:
        print(ele.get_text())
else:
    print("없음")