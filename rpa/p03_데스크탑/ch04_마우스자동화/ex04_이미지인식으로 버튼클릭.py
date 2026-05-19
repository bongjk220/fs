import pyautogui
from pathlib import Path

try:
    # 선택한 창만 캡쳐
    box = pyautogui.locateOnScreen("setting.png")
    print("box:", box)
    # box: Box(left=187, top=841, width=34, height=39)
    pyautogui.moveTo(box.left + box.width // 2, box.top + box.height // 2, duration=0.2)
    pyautogui.click()
except pyautogui.ImageNotFoundException:
    print("해당하는 이미지를 찾을 수 없습니다.")
except Exception as e:
    print("알수 없는 에러:", e)


try:
    items = list(pyautogui.locateAllOnScreen("folder.png"))
    
    print("items:", items)

    for i, b in enumerate(items):
        print(f"{i+1}번째 박스 : ", b)

except pyautogui.ImageNotFoundException:
    print("해당하는 이미지를 찾을 수 없습니다.")
except Exception as e:
    print("알수 없는 에러:", e)