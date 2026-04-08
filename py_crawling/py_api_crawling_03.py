# 서울시 공공데이터 API를 활용하여 대기질 정보를 크롤링하고 SQLite DB에 저장하는 예제 코드입니다.
import requests
import sqlite3
import schedule
import time

# DB 초기화
def init_db():
    conn = sqlite3.connect("air_quality.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS air_quality (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            region TEXT,
            station TEXT,
            PM INTEGER,
            FPM INTEGER,
            FPM INTEGER,
            FPM INTEGER
            saved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

def save_to_db(items):
    conn = sqlite3.connect("air_quality.db")
    cursor = conn.cursor()
    for p in items:
        cursor.execute("""
            INSERT INTO air_quality (region, station, PM, FPM) VALUES (?, ?, ?, ?)
        """, (p["region"], p["station"], p["PM"], p["FPM"]))
    conn.commit()
    conn.close()

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
    #print(json.dumps(data, indent=2, ensure_ascii=False))
    items = []
    for row in data.get("RealtimeCityAir", {}).get("row", []):
        items.append({
            "region": row.get("SAREA_NM"),   # 지역명
            "station": row.get("MSRSTN_NM"), # 측정소명
            "PM": row.get("PM"),             # 미세먼지(단위:㎍/㎥)
            "FPM": row.get("FPM"),           # 초미세먼지(단위:㎍/㎥)
            "OZON": row.get("OZON"),         # 오존(단위:ppm)
            "CAI_GRD": row.get("CAI_GRD")    # 통합대기환경지수 등급
        })

    # save_to_db(items)
    print("데이터 저장 완료:", items)

# DB 초기화
# init_db()

# 1분마다 실행
schedule.every(1).minutes.do(crawl_air_quality)

while True:
    schedule.run_pending()
    time.sleep(1)