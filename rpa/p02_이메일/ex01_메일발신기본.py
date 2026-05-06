import smtplib # 내장모듈
from account import * # 방금만든 account.py

try:
    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.ehlo() # smtp server에 접속 확인
        smtp.starttls() # 모든 내용이 암호화되어 전송
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD) # 로그인

        subject = "Test Email" # 메일 제목
        body = "This is a test email" # 메일 본문
        # subject = "테스트 메일" # 메일 제목
        # body = "한글일때는  'ascii' codec can't encode characters 오류남" # 메일 본문

        msg = f"Subject: {subject}\n{body}" # 메일 합치기

        # smtp.sendmail(발신자, 수신자, 메시지)
        smtp.sendmail(EMAIL_ADDRESS, "bjk001ai@gmail.com", msg)
        #smtp.sendmail(EMAIL_ADDRESS, "bjk001ai@gmail.com", msg.as_string())
        print("메일 전송 성공!")
except Exception as e:
    print("메일 전송 실패:", e)

# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# from account import EMAIL_ADDRESS, EMAIL_PASSWORD

# # 메일 제목과 본문
# subject = "Test Email"
# body = "This is a test email"

# # 메시지 객체 생성
# msg = MIMEMultipart()
# msg["From"] = EMAIL_ADDRESS
# msg["To"] = "whyeil29@gmail.com"
# msg["Subject"] = subject

# # 본문 추가
# msg.attach(MIMEText(body, "plain"))

# try:
#     with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
#         smtp.ehlo()
#         smtp.starttls()
#         smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
#         smtp.sendmail(EMAIL_ADDRESS, "whyeil29@gmail.com", msg.as_string())
#         print("메일 전송 성공!")
# except Exception as e:
#     print("메일 전송 실패:", e)
