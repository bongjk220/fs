# 안정적인 이미지 처리
import pyautogui

img_name = "버튼.png"

pyautogui.alert("대상 버튼을 캡쳐해 '버튼.png'로 저장 하세요.\n 확인을 누르면 3초 후 탐색을 시작합니다.")
pyautogui.countdown(3)

try:
    pyautogui.click(img_name)
    print("click()함수로... 클릭 성공!")
except pyautogui.ImageNotFoundException:
    print("locateOnScreen()함수로 재시도...")
    try:
        box = pyautogui.locateOnScreen(img_name)
        pyautogui.click(box.left + box.width // 2, box.top + box.height // 2, duration=0.2)
        print("locateOnScreen()함수로 클릭 성공!")
    except pyautogui.ImageNotFoundException:
        print("발견 실패")
        exit(1)
except Exception as e:
    print("알수 없는 에러:", e)
    exit(1)

try:
    # pyautogui.moveTo(img_name)
    pyautogui.dragTo(img_name)
except pyautogui.ImageNotFoundException:
    print("해당 이미지를 찾을 수 없습니다.")
except Exception as e:
    print("알수 없는 에러:", e)


print("끝!")