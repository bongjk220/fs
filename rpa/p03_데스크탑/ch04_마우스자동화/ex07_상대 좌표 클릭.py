'''
>python
>>> import pyautogui
>>> pyautogui.mouseInfo()
>>> quit()
'''
import pyautogui

pyautogui.countdown(3)

# 그림판 최대화면에서 좌표 찾기, 같은 해상도
# 브러쉬: 381,100 235,235,235 #EBEBEB
# Red: 839,81 237,28,36 #ED1C24 -> 611, 90

wins = pyautogui.getWindowsWithTitle("그림판")

win = wins[0]
print(win)
# <Win32Window left="17", top="173", width="1129", height="801", title="제목 없음 - 그림판">
print(win.left, win.top) # 17 173
pyautogui.moveTo(win.left + 381, win.top + 100, duration=0.5)
pyautogui.click()

pyautogui.sleep(1)

pyautogui.moveTo(win.left + 840, win.top + 65, duration=0.5)
pyautogui.sleep(1)
pyautogui.click()