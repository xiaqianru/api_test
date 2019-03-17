'''执行所有用例'''
import unittest
import os
import logging
import click
from lib.htmlrunner import HTMLTestRunner
from config import basedir,is_send
from lib.e_mail import send_email

@click.command()
@click.option("--send",default="false",help="是否发送邮件")
@click.option("--output",help="输出的文件名")
@click.option("--s",default=all,help="输出的文件名")

def run_all(send):
    suite = unittest.defaultTestLoader.discover(os.path.join(basedir,"testcase"))
    report_file = os.path.join(basedir,'report','report.html')
    logging.info("===========测试开始执行==========")
    with open(report_file,"wb") as f:
        HTMLTestRunner(stream=f,title="接口测试报告",description="longtengtester").run(suite)
    logging.info("===========测试执行结束==========")
    if is_send or send == "true":
        send_email(report_file)

if __name__ == '__main__':
    run_all()