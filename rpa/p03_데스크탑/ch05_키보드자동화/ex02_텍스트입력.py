import pyautogui
import pyperclip

pyautogui.alert("메모장을 실행 시켜 주세요. 확인을 누르면 실행 됩니다.")


# 메모장 열기
# import subprocess
# subprocess.Popen(["notepad.exe"])

pyautogui.sleep(1)
pyautogui.click()
pyautogui.write("Hello Python!", interval=0.1)
pyautogui.press("enter")

pyautogui.write(['a', 'b', 'left', 'left', 'X', 'Y', 'enter'], interval=0.1)

# 조합키 사용
pyautogui.keyDown("ctrl")
pyautogui.keyDown("a")
pyautogui.sleep(0.2)
pyautogui.keyUp("a")
pyautogui.keyUp("ctrl")

pyautogui.keyDown("ctrl")
pyautogui.keyDown("c")
pyautogui.sleep(0.2)
pyautogui.keyUp("c")
pyautogui.keyUp("ctrl")

pyautogui.press("end")
pyautogui.press("enter")

# pyautogui.keyDown("ctrl")
# pyautogui.keyDown("v")
# pyautogui.sleep(0.2)
# pyautogui.keyUp("v")
# pyautogui.keyUp("ctrl")

pyautogui.hotkey("ctrl", "v")

def send_text(text):
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl", "v")

pyautogui.write("파이썬, 자동화! 프로그래밍", interval=0.1)
send_text("파이썬 자동화 프로그래밍\n")

txt = "자동으로 써지네\n"
for c in txt:
    send_text(c)
    pyautogui.sleep(0.1)

name = pyautogui.prompt("성명을 입력해 주세요!")

if name:
    name = name + "님 어서 오세요."
    for c in name:
        send_text(c)
        pyautogui.sleep(0.1)

print("끝!")