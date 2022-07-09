import os
import unittest
from HTMLTestRunner import HTMLTestRunner
import time
from BeautifulReport import BeautifulReport
from common.send_email import SendEmail

if __name__ == '__main__':
    # suite = unittest.TestSuite()
    # suite.addTest(TestLogin('test_01_login_1'))
    # suite.addTests(unittest.TestLoader().loadTestsFromTestCase(Test2))
    suite = unittest.defaultTestLoader.discover(os.getcwd(), "test_login.py")
    nowtime = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime())
    # files = open(os.getcwd() + "/" + nowtime + "report.html", "wb")
    # runner = HTMLTestRunner(stream=files, verbosity=2, title="自动化测试报告", description="报告详情如下：")
    # runner.run(suite)
    report_name = os.path.dirname(__file__) + '/Report/report' + nowtime + '.html'
    BeautifulReport(suite).report(description="自动化测试报告", filename="report" + nowtime, log_path="Report")
    # 在发送邮件之前一定要把文件流关闭
    # files.close()
    SendEmail().send_email(report_name)
