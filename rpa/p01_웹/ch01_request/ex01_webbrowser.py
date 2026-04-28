import webbrowser # 내장 모듈

search_query = "RPA"
naver_search_url = "https://search.naver.com/search.naver?query=" + search_query

webbrowser.open(naver_search_url)



keywords = ["메가박스", "CGV", "롯데시네마"]

for query in keywords:
    url = "https://search.naver.com/search.naver?query=" + query
    webbrowser.open(url)