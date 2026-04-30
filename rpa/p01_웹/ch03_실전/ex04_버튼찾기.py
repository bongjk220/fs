# '이전' 버튼 링크 찾기
'''
<a rel="prev" href="/3236/" accesskey="p">&lt; Prev</a>
<a rel="next" href="#" accesskey="n">Next &gt;</a>
a 태그 -> rel == "prev"
[속성명='속성값'] -> "a[rel='prev']" -> 요소.get
'''
'''
prev 버튼에서 오른쪽 마우스 > 검사 > 해당 선택라인에서 오른쪽 마우스 > Copy > Copy Element
<a rel="prev" href="/3235/" accesskey="p">&lt; Prev</a>

next 버튼에서 오른쪽 마우스 > 검사 > 해당 선택라인에서 오른쪽 마우스 > Copy > Copy Element
<a rel="next" href="/3237/" accesskey="n">Next &gt;</a>
'''

import requests, bs4

target_url = "https://xkcd.com/3236/"

response = requests.get(target_url, timeout=10)
response.raise_for_status()

soup = bs4.BeautifulSoup(response.text, "html.parser")

prev_link_element = soup.select("a[rel='prev']")
print(prev_link_element) # [<a accesskey="p" href="/3235/" rel="prev">&lt; Prev</a>, <a accesskey="p" href="/3235/" rel="prev">&lt; Prev</a>]
print(prev_link_element[0]) # <a accesskey="p" href="/3235/" rel="prev">&lt; Prev</a>

if not prev_link_element:
    print("이전 페이지 링크 없음")
else:
    # <a rel="prev" href="/3236/" accesskey="p">&lt; Prev</a>
    prev_path = prev_link_element[0].get("href")
    print(prev_path) # /3235/

    if not prev_path.startswith("http"):
        prev_path = "https://xkcd.com" + prev_path # https://xkcd.com/3235

    print("다음에 방문할 주소:", prev_path) # 다음에 방문할 주소: https://xkcd.com/3235/