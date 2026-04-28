import requests

target_url = "https://www.gutenberg.org/files/57362/57362-0.txt"

try: 
    response = requests.get(target_url)
    print("response:",response)
    response.raise_for_status() # (정상이 아닐경우) 강제 예외 발생위해

    cnt = 0
    # 윤동주_시.txt -> 387KB
    with open("윤동주_시.txt", "wb", encoding="utf-8") as my_file:
        # chunk_size = 100000 byte -> 약 100KB
        for chunk in response.iter_content(chunk_size=100000): # 한번에 불러오는 양을 정하는게 chrunk_size
            cnt += 1
            print(cnt)
            my_file.write(chunk)

except requests.exceptions.HTTPError as e:
    print("페이지 로딩 에러:", e)
else:
    print("페이지 로딩 성공:", response.status_code)