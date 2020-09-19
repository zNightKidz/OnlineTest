# coding=utf-8
import requests
import unittest
import json
import HTMLTestRunner
from HTMLTestRunner import HTMLTestRunner
import time
import os
import smtplib
from email.mime.text import MIMEText
from email.header import Header

import test_allFacility_get
#查找测试目录
def new_report(test_report):
    lists = os.listdir(test_report)
    lists.sort(key=lambda fn:os.path.getmtime(test_report+'\\'+fn))
    file_new = os.path.join(test_report,lists[-1])
    print("测试文件是：",file_new)
    return file_new


#发送邮件
def send_mail(file_new):
    f = open(file_new,'r',encoding='UTF-8')
    mail_body = f.read()
    f.close()

    msg = MIMEText(mail_body,'html','utf-8')
    msg['Subject'] = Header('接口自动化测试报告','utf-8')

    smtp = smtplib.SMTP()
    smtp.connect('smtp.163.com')
    smtp.login('zhangjinbo@ndtchina.com','zhjinbo2018!')
    smtp.sendmail('zhangjinbo@ndtchina.com','zhangjinbo@ndtchina.com',msg.as_string())
    smtp.quit()
    print('邮件已发出！')


if __name__ == "__main__":
    testunit = unittest.TestSuite()
    testunit.addTest(test_allFacility_get.test_allFacility_get("test_allFacility_get"))
    testunit.addTest(test_allFacility_get.test_allFacility_get("test_1"))
    testunit.addTest(test_allFacility_get.test_allFacility_get("test_2"))

    now = time.strftime("%Y-%m-%d %H-%M-%S")
    filename = './' + 'testresult.html'
    fp = open(filename,'w',encoding='UTF-8')

    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title = "接口测试报告",description = "测试用例执行情况")
    runner.run(testunit)
    fp.close()

    test_report = 'E:/python test/UnicomTest'
    new_report = new_report(test_report)
    send_mail(new_report)