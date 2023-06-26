import os
import sys
import smtplib
from email.mime.text import MIMEText

# 获取环境变量
email_address = os.environ['FASTMRT_EMAIL']
email_password = os.environ['FASTMRT_EMAIL_PASSWARD']

# 获取命令行参数
name = sys.argv[1]
email = sys.argv[2]
message = sys.argv[3]

# 构造邮件内容
subject = 'New commit on GitHub'
body = f'Dear {name},\n\nA new commit has been made on your GitHub repository. The commit message is "{message}".\n\nBest regards,\nYour team'
msg = MIMEText(body)
msg['Subject'] = subject
msg['From'] = email_address
msg['To'] = email

# 发送邮件
smtp = smtplib.SMTP('smtp.gmail.com', 587)
smtp.ehlo()
smtp.starttls()
smtp.login(email_address, email_password)
smtp.sendmail(email_address, email, msg.as_string())
smtp.quit()