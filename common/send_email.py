import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.header import Header
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase


class SendEmail:
    @classmethod
    def send_email(cls, report_name):
        smtp_server = 'smtp.qq.com'
        username = '841042124@qq.com'
        password = 'bxirbkxeyumybfej'
        receiver = ['841042124@qq.com', '2111570372@qq.com', '1752850304@qq.com']
        content = """
        <h1>图片内容:</h1>
        <img src='cid:img1'>
        """
        msg = MIMEMultipart()
        msg['Subject'] = '发送测试报告'
        msg['From'] = username
        msg['To'] = ','.join(receiver)  # 给多人发送邮箱

        # 以html发送图片正文
        # img_data = open('img/test_01_login.pnga', 'rb').read()
        # img = MIMEImage(img_data)
        # img.add_header('Content-ID', '<img1>')
        # msg.attach(img)

        # msg.attach(MIMEText(content, 'html', 'utf-8'))
        # 发送附件
        attchment = MIMEBase('application', 'octet-stream')
        attchment.set_payload(open(report_name, 'rb').read())
        attchment.add_header('Content-Disposition', 'attachment', filename=Header(report_name, 'utf-8').encode())
        encoders.encode_base64(attchment)
        msg.attach(attchment)

        # 连接和登录
        smtp = smtplib.SMTP_SSL(smtp_server, 465)
        smtp.login(username, password)
        # 发送邮件
        smtp.sendmail(username, receiver, msg.as_string())
        smtp.quit()
