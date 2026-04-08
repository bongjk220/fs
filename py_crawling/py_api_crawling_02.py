# 서울시 공공데이터 API를 활용하여 실시간 대기질 정보를 크롤링하는 예제 코드입니다. 1분마다 API를 호출하여 데이터를 출력합니다.
import requests
import json
import schedule
import time

def crawl_air_quality():
    # url = "http://openapi.seoul.go.kr:8088/sample/json/RealtimeCityAir/1/5/" # 서울 열린데이터광장 샘플 API(서울시 실시간 대기질 데이터)
    # url = "http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=1159068000" # 기상청 RSS 데이터 API(특정 지역의 단기예보를 RSS/XML로 제공)
    # url = "https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY" # NASA Open API (DEMO_KEY)
    # url = "https://api.openweathermap.org/data/2.5/weather?q=Seoul&appid=demo" # OpenWeatherMap (무료 tier)
    url = "http://openapi.seoul.go.kr:8088/sample/json/RealtimeCityAir/1/5/"
    response = requests.get(url)
    if response.status_code != 200:
        print("API 요청 실패:", response.status_code)
        return

    data = response.json()
    # 응답 구조 확인 (디버깅용)
    print(json.dumps(data, indent=2, ensure_ascii=False))

    for row in data.get("RealtimeCityAir", {}).get("row", []):
        print(f"지역: {row.get('MSRSTN_NM')}, PM: {row.get('PM')}, OZON: {row.get('OZON')}")

# 1분마다 실행
schedule.every(1).minutes.do(crawl_air_quality)

while True:
    schedule.run_pending()
    time.sleep(1)