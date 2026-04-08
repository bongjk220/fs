# 서울시 공공데이터 API를 활용하여 약국 정보를 크롤링하고 SQLite DB에 저장하는 예제 코드입니다.
import requests
import sqlite3
import schedule
import time

API_KEY = "YOUR_SERVICE_KEY"  # 발급받은 서비스키 입력
BASE_URL = "http://openapi.seoul.go.kr:8088"

# DB 초기화
def init_db():
    conn = sqlite3.connect("public_data.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pharmacies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            address TEXT,
            phone TEXT,
            saved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

def save_to_db(items):
    conn = sqlite3.connect("public_data.db")
    cursor = conn.cursor()
    for p in items:
        cursor.execute("""
            INSERT INTO pharmacies (name, address, phone) VALUES (?, ?, ?)
        """, (p["name"], p["address"], p["phone"]))
    conn.commit()
    conn.close()

def crawl_public_data():
    url = f"{BASE_URL}/{API_KEY}/json/PharmacyInfo/1/20"  
    # PharmacyInfo는 예시 API, 1~20은 가져올 데이터 범위

    response = requests.get(url)
    if response.status_code != 200:
        print("API 요청 실패:", response.status_code)
        return

    data = response.json()
    items = []
    for row in data.get("PharmacyInfo", {}).get("row", []):
        items.append({
            "name": row.get("NM"),
            "address": row.get("ADDR"),
            "phone": row.get("TEL")
        })

    save_to_db(items)
    print("데이터 저장 완료:", items)

# DB 초기화
init_db()

# 매일 09시에 실행
schedule.every().day.at("09:00").do(crawl_public_data)

while True:
    schedule.run_pending()
    time.sleep(60)