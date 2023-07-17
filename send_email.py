import os
import sys
import smtplib
from email.mime.text import MIMEText
from contextlib import contextmanager
import datetime

@contextmanager
def send_email(email_address, email_password):
    smtp = smtplib.SMTP_SSL('smtp.qq.com')
    smtp.connect('smtp.qq.com', 465)
    smtp.login(email_address, email_password)
    yield smtp
    smtp.quit()


if __name__ == '__main__':
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # 获取环境变量
    send_email_address = os.environ['FASTMRT_EMAIL']
    send_email_password = os.environ['FASTMRT_EMAIL_PASSWARD']
    reminder_email_address = os.environ['FASTMRT_REMINDER_EMAIL']
    full_dataset_link = os.environ['FASTMRT_FULL_DATASET']
    source_dataset_link = os.environ['FASTMRT_SOURCE_DATASET']
    diffusion_augment_dataset_link = os.environ['FASTMRT_DIFFUSION_AUGMENT_DATASET']

    # 获取命令行参数
    name = sys.argv[1]
    to_email = sys.argv[2]
    institution = sys.argv[3]

    # 获取环境变量
    # send_email_address = 'fastmrt@foxmail.com'
    # send_email_password = 'hzdljncxwglahbia'
    # reminder_email_address = 'fastmr.thermometry@gmail.com'

    # # 获取命令行参数
    # name = 'sijie xu'
    # to_email = 'sijie.x@sjtu.edu.cn'
    # institution = 'SJTU'

    # send back message
    main_subject = 'FastMRT Dataset Download Links'
    main_body = f"Dear {name},\n\nThank you for applying for our dataset. "\
                f"We're happy to provide you with the following links:\n\n- Full dataset: {full_dataset_link}\n" \
                f"- Source dataset: {source_dataset_link}\n- Diffusion augment dataset: {diffusion_augment_dataset_link}\n\n" \
                f"Please note that you need to comply with our data sharing policy, which can be found at https://fastmrt.github.io/. "\
                f"If you have any questions, please feel free to contact us.\n\nBest regards,\nFastMRT Team"
    main_msg = MIMEText(main_body)
    main_msg['Subject'] = main_subject
    main_msg['From'] = send_email_address
    main_msg['To'] = to_email

    # send reminder message
    reminder_subject = 'FastMRT Dataset Request Information Record'
    reminder_body = f'There is a new dataset request. The record is as follows:\n\n- Applicant: {name}\n- Institution: {institution}\n- Recipient email address: {to_email}\n- Time: {current_time}'
    reminder_msg = MIMEText(reminder_body)
    reminder_msg['Subject'] = reminder_subject
    reminder_msg['From'] = send_email_address
    reminder_msg['To'] = reminder_email_address

    # 发送邮件
    with send_email(send_email_address, send_email_password) as smtp:
        smtp.sendmail(send_email_address, to_email, main_msg.as_string())
        smtp.sendmail(send_email_address, reminder_email_address, reminder_msg.as_string())



