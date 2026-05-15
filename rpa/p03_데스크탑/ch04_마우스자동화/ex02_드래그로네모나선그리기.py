import subprocess, pyautogui


# 실행 -> 5초 대기 -> 그림판 전환 -> 클릭
print("그림판으로 전환해 주세요.")

# 그림판 실행
# os.system("mspaint") # os.system은 명령어 실행 후 다음 명령어로 넘어가기 전에 명령어가 끝날 때까지 기다린다.
subprocess.Popen("mspaint")
pyautogui.sleep(0.5)

# 그림판 창 최대화 (윈도우 단축키)
pyautogui.hotkey("win", "up")

# pyautogui.sleep(5)
pyautogui.countdown(1)

# 캔버스 시작 위치로 이동 (좌표는 해상도에 맞게 조정)
start_x, start_y = 200, 200
pyautogui.moveTo(start_x, start_y)
pyautogui.click()  # 시작점 클릭

dist = 300
step = 20
count = 0

while dist > 0:
    pyautogui.drag(dist, 0, duration=0.1)   # 오른쪽
    dist -= step
    pyautogui.drag(0, dist, duration=0.1)   # 아래
    pyautogui.drag(-dist, 0, duration=0.1)  # 왼쪽
    dist -= step
    pyautogui.drag(0, -dist, duration=0.1)  # 위