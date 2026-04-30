# 명시적 대기(Explicit Waits)
'''
WebDriverWait()
http://localhost:63342/rpa/ch02_%EC%9B%B9%EC%8A%A4%ED%81%AC%EB%9E%98%ED%95%91/05_selenium%EC%8B%AC%ED%99%94/ex01_app.html?_ijt=5rs2ngl6hpm4jspm1mh0dcjn3k&_ij_reload=RELOAD_ON_SAVE
'''
'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Selenium Explicit Wait Test</title>
    <script>
        function showMessage() {
            // 버튼 클릭 후 3초 뒤 <h2>Hello</h2> 추가
            setTimeout(() => {
                const h2 = document.createElement('h2');
                //<h2></h2>
                h2.textContent = 'Hello';
                document.body.appendChild(h2);
                //<h2>Hello</h2>
            }, 3000);
        }
    </script>
</head>
<body>
    <h1>명시적 대기 실습</h1>
    <p>버튼을 누르면 3초 뒤에 "Hello"가 나타납니다.</p>
    <button onclick="showMessage()">Try it</button>
</body>
</html>
'''
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
# browser.get("http://127.0.0.1:5500/rpa/p01_웹/ch04_셀레니엄/ex07_app.html")
browser.get(r"C:\bong\git\fs\rpa\p01_웹\ch04_셀레니엄\ex07_app.html") # 됨
# browser.get(r"rpa\p01_웹\ch04_셀레니엄\ex07_app.html") # 안됨
time.sleep(2)

try:
    try_it_button = browser.find_element(By.TAG_NAME, 'button') # find_elements는 try 필요없음
    try_it_button.click()
    print("버튼 클릭 완료")

    # WebDriverWait는 try가 필요
    # WebDriverWait(browser, 10): 브라우저야, 최대 10초 동안 기다려줄게
    # .until(...): "...할 때까지!"
    # EC.presence_of_element_located(...): "DOM 안에 해당 요소가 존재(presence)할 때까지."
    # (By.XPATH, '//h2[text()="Hello"]'): "찾을 대상은 텍스트가 'Hello'인 <h2> 태그야."
    hello_element = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//h2[text()="Hello"]')))
    # F12 > "Hello" 부분 오른쪽 마우스 > 검사 > copy > copy xpath # /html/body/h2

    print("찾은 요소: ", hello_element.text) # Hello

except Exception as e:
    print("에러:",e)

time.sleep(10)
browser.quit()