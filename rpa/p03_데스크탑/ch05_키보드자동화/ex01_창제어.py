import sys
import pyautogui

print(pyautogui.getAllWindows())
# dow(hWnd=920228), Win32Window(hWnd=131268), Win32Window(hWnd=789598), Win32Window(hWnd=330252), Win32Window(hWnd=68016), Win32Window(hWnd=68008), Win32Window(hWnd=131212), Win32Window(hWnd=198032), Win32Window(hWnd=197322), Win32Window(hWnd=66056), Win32Window(hWnd=66046), Win32Window(hWnd=66028), Win32Window(hWnd=66000), Win32Window(hWnd=65998), Win32Window(hWnd=65996), Win32Window(hWnd=65994), Win32Window(hWnd=65942)]

# OS 판별
'''
'darwin': macOS
'win32': Windows
'linux': Linux
'''
if not sys.platform.startswith("win"):
    print("이 프로그램은 윈도우에서만 작동 합니다.")
    print("대신 창 제목만 나열합니다.")
    print(pyautogui.getAllWindows())
    sys.exit()


print("-" * 30)
# 메모장의 핸들 가져오기(title...)
wins = pyautogui.getWindowsWithTitle("메모장")
print(wins) # [Win32Window(hWnd=2886594)]

if not wins:
    print("메모장을 열어주세요. 잠시 대기합니다.")
    pyautogui.countdown(5)
    wins = pyautogui.getWindowsWithTitle("메모장")

if not wins:
    print("창을 찾기 못했습니다.")
    exit(1)

win = wins[0]
print(win) 
# <Win32Window left="-1881", top="250", width="1532", height="675", title="메모장">
print("창 제목:", win.title) # 창 제목: 연습.txt - 메모장
print("현재 위치:", win.left, win.top) # 현재 위치: -1881 250
print("현재 위치2:", win.topleft) # 현재 위치2: Point(x=-1881, y=250)
print("창 크기:", win.width, win.height) # 창 크기: 1532 675
print("창 크기2:", win.size) # 창 크기2: Size(width=1532, height=675)

win.activate() # 활성화(맨 앞으로 가져오기)
pyautogui.sleep(1)
win.width = 800
win.height = 200

pyautogui.sleep(1)
win.topleft = (100, 100) # 사이즈 변경 크기

if not win.isMaximized:
    win.maximize()  # 최대 크기

pyautogui.sleep(1)
win.restore() # 중간 크기

pyautogui.sleep(1)

win.close() # 창닫기