# pip install pyautogui
import platform
import pyautogui

# 프로그램을 강제 종료 시키려면 마우스를 화면 끝으로 이동시킨다.
pyautogui.PAUSE = 0.2

size = pyautogui.size()
print(f"접근 가능 영역 x: 0~{size.width-1}, y: 0~{size.height-1}") # 접근 가능 영역 x: 0~1919, y: 0~1079

# 현재 마우스 좌표 읽기
pos = pyautogui.position()
print("현재 위치: ", pos) # 현재 위치:  Point(x=1349, y=490)

# for i in range(1):
#     # 절대 좌표 이동
#     # pyautogui.moveTo(x좌표, y좌표, 이동시간)
#     pyautogui.moveTo(100, 100, duration=0.5)
#     pyautogui.moveTo(1000, 100, duration=0.5)
#     pyautogui.moveTo(1000, 1000, duration=0.5)
#     pyautogui.moveTo(100, 1000, duration=0.5)

# pyautogui.moveTo(pos.x, pos.y, duration=0.5) # 현재 위치

# 상대 좌표 이동
# pyautogui.move(100, 0, duration=0.5)
# pyautogui.move(0, 100, duration=0.5)
# pyautogui.move(-100, 0, duration=0.5)
# pyautogui.move(0, -100, duration=0.5)

# 마우스 클릭
# 현재 위치: pyautogui.click()
# pyautogui.click()

# pyautogui.click(x좌표, y좌표)
# moveTo + click
# pyautogui.click(1000, 500, duration=0.5)

# scroll
pyautogui.scroll(500) # 위로
pyautogui.sleep(5)
pyautogui.scroll(-500) # 아래로
pyautogui.sleep(5)
pyautogui.scroll(-500) # 아래로
pyautogui.scroll(500) # 위로
pyautogui.sleep(5)
pyautogui.scroll(500) # 위로
pyautogui.sleep(5)
pyautogui.scroll(-500) # 위로
pyautogui.sleep(5)
print("platform:", platform.system()) # platform: Windows