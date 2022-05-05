import smtplib
from email.message import EmailMessage

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465

message = EmailMessage()
message.set_content("본문입니다.")

message["Subject"] = "이것은 제목입니다."
message["From"] = "shpark9349@gmail.com"
message["To"] = "shpark9346@naver.com"

smtp = smtplib.SMTP_SSL(SMTP_SERVER,SMTP_PORT)
smtp.login("shpark9349@gmail.com","s4637746377*")
smtp.send_message(message)
smtp.quit()