import requests

url = "https://www.python.org"
response = requests.get(url)
print("response:",response) # response: <Response [200]>
print("페이지 로딩 성공",response.status_code) # 페이지 로딩 성공 200