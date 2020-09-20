# coding=utf-8

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from email.header import Header

my_sender = 'zjinbo_0311@163.com'

my_receiver = '402248867@qq.com'


def mail():
    ret = True
    try:


        #msg = MIMEText('接口测试报告','plain','utf-8')

        mail_body = """<p>自动化测试报告</p>
        <p><a href="E:/python test/UnicomTest/testresult.html">这是报告链接</a><P>
        """
        msg = MIMEText(mail_body, 'html', 'utf-8')
        msg['From'] = formataddr(["测试工程师",my_sender])
        msg['To'] = formataddr(["运维接收人",my_receiver])
        msg['Subject'] = "今日测试报告"

        server = smtplib.SMTP('smtp.163.com', 25)
        server.login(my_sender, "1175233452zjb")

        server.sendmail(my_sender, my_receiver, msg.as_string())
        server.quit()
    except Exception:
        ret = False

    return ret


ret = mail()

if ret:
    print("邮件已经发送！")
else:
    print("发送失败！")
