"""发送邮件"""
import smtplib
import logging
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import email_config


# # 纯文本格式邮件
# # 1.组装邮件正文
# msg = MIMEText("hi,这是一封邮件","plain","utf-8")  # plain是纯文本/html
# #2.组装邮件头
# msg["From"] = "test_results@sina.com"
# msg["To"] = "63829186@qq.com"
# msg["Subject"] = "接口测试报告"
# #3. 连接smtp服务器并发送邮件
# smtp = smtplib.SMTP_SSL("smtp.sina.com")    # 连接smtp服务器
# smtp.login(msg["From"],"hanzhichao123")  # 邮箱账户和密码
# smtp.sendmail(msg["From"],msg["To"],msg.as_string())
#

def send_email(report_file):
    #带附件的邮件格式
    # 1.组装邮件正文
    msg = MIMEMultipart()  # plain是纯文本/html
    body = MIMEText(email_config["body"],"plain","utf-8")
    msg.attach(body)

    #2.组装邮件头
    msg["From"] = email_config["user"]
    msg["To"] = email_config["receiver"]
    msg["Subject"] = email_config["subject"]

    # 3.添加附件
    attr = MIMEText(open(report_file,"rb").read(),"base64","utf-8")   #内容读出来，用utf-8解码，再用base64编码
    attr["Content-Type"]= "application/octet-stream"   # 二进制数据流格式，固定  内容类型
    attr["Content-Disposition"] = "attachment; filename ='report.html'"
    msg.attach(attr)

    #4. 连接smtp服务器并发送邮件
    smtp = smtplib.SMTP(email_config["server"])    # 连接smtp服务器
    smtp.login(msg["From"], email_config["password"])  # 邮箱账户和密码
    smtp.sendmail(msg["From"], msg["To"], msg.as_string())
    logging.info("发送邮件完成")



