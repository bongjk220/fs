from imap_tools import MailBox
from account import *

# with문을 사용하지 않을 경우 : with문을 사용할 경우 logout을 할 필요가 없다.
# mailbox = MailBox("imap.gmail.com", 993)
# mailbox.login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX")
# mainbox.logout()

with MailBox("imap.gmail.com", 993) as mailbox:
    mailbox.login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX")

    # 전체 메일 가져오기
    # for msg in mailbox.fetch():
    #     print("[{}] {}".format(msg.from_, msg.subject))

    # 최근 5개 메일 가져오기
    # for msg in mailbox.fetch(limit=5, reverse=True):
    #     print("[{}] {}".format(msg.from_, msg.subject))

    # 읽지 않은 메일 가져오기
    # for msg in mailbox.fetch('(UNSEEN)'):
    #     print("[{}] {}".format(msg.from_, msg.subject))

    # 특정인이 보낸 메일 가져오기
    # for msg in mailbox.fetch('(FROM bjk001ai@gmail.com)', reverse=True, limit=3):
    #     print("[{}] {}".format(msg.from_, msg.subject))

    # 특정 글자를 포함하는 메일(제목, 본문) 가져오기
    # '(TEXT "test mail")' -> 작은 따옴표로 감싸고, 검색 글자를 큰 따옴표로 감싼다.
    # -> test, mail 각각의 단어를 포함하는 메일을 검색한다.
    # for msg in mailbox.fetch('(TEXT "Ultra S20")', reverse=True, limit=3):
    #     print("[{}] {}".format(msg.from_, msg.subject))

    # 특정 글자를 포함하는 메일(제목만) 가져오기
    # for msg in mailbox.fetch('(SUBJECT "Ultra S20")', reverse=True, limit=3):
    #     print("[{}] {}".format(msg.from_, msg.subject))

    # 특정 글자를 한글을 포함하는 메일(제목만) 가져오기
    # for msg in mailbox.fetch(limit=5, reverse=True):
    #     if "테스트" in msg.subject:
    #         print("[{}] {}".format(msg.from_, msg.subject))

    # 2026년 5월 1일 이후의 메일 가져오기
    # for msg in mailbox.fetch('(SENTSINCE 01-MAY-2026)', reverse=True, limit=3):
    #     print("[{}] {}".format(msg.from_, msg.subject))

    # 2026년 5월 4일에 온 메일 가져오기
    # for msg in mailbox.fetch('(ON 04-MAY-2026)', reverse=True, limit=3):
    #     print("[{}] {}".format(msg.from_, msg.subject))

    # 두 가지 이상의 조건을 모두 만족하는(그리고) 메일 가져오기(AND)
    # for msg in mailbox.fetch('(ON 04-MAY-2026 SUBJECT "Ultra")', reverse=True):
    #     print("[{}] {}".format(msg.from_, msg.subject))

    print("="*50)

    # 두 가지 이상의 조건 중 하나라도 만족하는(또는) 메일 가져오기(OR)
    for msg in mailbox.fetch("(OR ON 04-MAY-2026 SUBJECT 'test')", reverse=True, limit=3):
        print("[{}] {}".format(msg.from_, msg.subject))