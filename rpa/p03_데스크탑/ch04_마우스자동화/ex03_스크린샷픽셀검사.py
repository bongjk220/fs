import pyautogui

# 색상 읽기
# pyautogui.pixel(x좌표, y좌표)
rgb1 = pyautogui.pixel(10, 10)
print(rgb1) # (227, 227, 232)
rgb2 = pyautogui.pixel(11, 11)

# 모니터 전체 화면 캡쳐
im = pyautogui.screenshot('screen.png')

isMatch = pyautogui.pixelMatchesColor(10, 10, rgb1)
print(isMatch) # True

if not pyautogui.pixelMatchesColor(200, 150, rgb1):
    print("물약")
    # 물약 클릭

im.save('screen2.png')