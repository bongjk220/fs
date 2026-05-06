import smtplib, os
from account import *
from email.message import EmailMessage

msg = EmailMessage()
msg["Subject"] = "테스트 메일" # 메일 제목
msg["From"] = EMAIL_ADDRESS     # 발신자
msg["To"] = "bjk001ai@gmail.com" # 수신자

msg.set_content("첨부 파일을 포함한 메일입니다.") # 메일 본문

# 현재 실행 중인 파이썬 파일의 폴더 경로를 가져옵니다.
current_path = os.path.dirname(__file__) # c:\bong\git\fs\rpa\p02_이메일
file_path1 = os.path.join(current_path, "python.png") # c:\bong\git\fs\rpa\p02_이메일\python.png
file_path2 = os.path.join(current_path, "테스트.pdf") # c:\bong\git\fs\rpa\p02_이메일\테스트.pdf
file_path3 = os.path.join(current_path, "테스트.xlsx") # c:\bong\git\fs\rpa\p02_이메일\테스트.xlsx

try:
    # MIME-Type: image/png, application/pdf, application/octet-stream
    # msg.add_attachment("python.png")
    # 첨부 파일 적용
    with open(file_path1, "rb") as f:
        msg.add_attachment(f.read(), maintype="image", subtype="png", filename=f.name)
    with open(file_path2, "rb") as f:
        msg.add_attachment(f.read(), maintype="application", subtype="pdf", filename=f.name)
    with open(file_path3, "rb") as f:
        msg.add_attachment(f.read(), maintype="application", subtype="octet-stream", filename=f.name)

    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.ehlo() # smtp server에 접속 확인
        smtp.starttls() # 모든 내용이 암호화되어 전송
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD) # 로그인
        smtp.send_message(msg)
        print("메일 전송 성공!")
except Exception as e:
    print("메일 전송 실패:", e)