'''
<div id="comic">
<img src="//imgs.xkcd.com/comics/husband_and_wife.png" title="Borat came out twenty years ago this year--closer to the breakup of the Soviet Union than to today--but it honestly feels like it's been even longer, somehow." alt="Husband and Wife" srcset="//imgs.xkcd.com/comics/husband_and_wife_2x.png 2x" style="image-orientation:none">
</div>
'''

import requests, os, bs4

#target_url = "https://xkc111d.com"
target_url = "https://123456"

# 현재 실행 중인 .py 파일의 절대 경로를 가져옵니다.
current_file_path = os.path.abspath(__file__)
print(current_file_path)
# 그 파일이 들어있는 '폴더' 경로만 추출합니다.
current_dir = os.path.dirname(current_file_path)
print(current_dir)

save_path = os.path.join(current_dir, "img")
print(save_path)

# 2. 이미지 저장 폴더 지정
os.makedirs(save_path, exist_ok=True)

# 3. 크롤링
try:
    response = requests.get(target_url)
    response.raise_for_status()

    soup = bs4.BeautifulSoup(response.text, "html.parser")
    img_ele_list = soup.select("#comic img")
    print(img_ele_list)
    '''
        [<img alt="Soniferous Aether" src="//imgs.xkcd.com/comics/soniferous_aether.png" srcset="//imgs.xkcd.com/comics/soniferous_aether_2x.png 2x" style="image-orientation:none" title="Imagine you could ride alongside a sound wave. It would probably be pretty cool, right? We're putting in a departmental budget request to buy a really fast plane so we can check it out."/>]
    '''
    print(len(img_ele_list))

    if not img_ele_list:
        print("만화 이미지가 없습니다.")
    else:
        image_url = img_ele_list[0].get("src")
        print(image_url) # //imgs.xkcd.com/comics/soniferous_aether.png

        if not image_url.startswith("http"):
            image_url = "https:" + image_url

        print(image_url) # https://imgs.xkcd.com/comics/soniferous_aether.png

        # 이미지 데이터 요청
        res_img = requests.get(image_url)
        res_img.raise_for_status()

        # 파일로 저장
        with open(save_path + "/xkcd_comic.png", "wb") as f:
            for chunk in res_img.iter_content(100000):
                f.write(chunk)
        print("이미지 저장 완료!")

#except requests.exceptions.HTTPError as e:
except Exception as e:
    print("에러:", e)
else:
    print("페이지 로딩 성공:", response.status_code) # 페이지 로딩 성공: 200
