import pyautogui

img_name = "logo.png"
pyautogui.countdown(3)

try:
    boxes = list(pyautogui.locateAllOnScreen(img_name))

    if not boxes:
        print("이미지를 찾을 수 없습니다.")
    else:
        mx, my = pyautogui.position()

        def center(b):return (b.left + b.width // 2, b.top + b.height // 2) # 박스의 중심점 좌표를 구하는 함수
        def dist(p):return (p[0] - mx) ** 2 + (p[1] - my) ** 2 # distance 가까운것을 찾는다. 제곱근을 구하지 않아도 비교는 가능

        centers = [center(b) for b in boxes]
        target = min(centers, key=dist)

        pyautogui.moveTo(target, duration=0.2)
        pyautogui.click()
        print("제일 가까운 점을 클릭했습니다.")

except pyautogui.ImageNotFoundException:
    print("이미지를 찾을 수 없습니다.")
except Exception as e:
    print("알수 없는 에러:", e)

print("끝")