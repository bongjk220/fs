import os
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

EMAIL_ADDRESS = os.getenv("EMAIL_ADDR")
EMAIL_PASSWORD = os.getenv("EMAIL_PASS")