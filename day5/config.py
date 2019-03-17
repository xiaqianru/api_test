'''项目的配置文件'''
import os
import logging
#路径配置
basedir = os.path.abspath(os.path.dirname(__file__))  # os.path.dirname(__file__)当前文件所在的绝对路径，os.path.abspath是绝对路径

#数据配置
db_config = {
    "host": "115.28.108.130",
    "port": 3306,
    "user": "test",
    "password": "123456",
    "db": "longtengserver",
    # "autocommit": True
}

#日志配置  level：日志级别，fromat：日志输出格式，datefmt：日期格式 handers：日志输出处理器

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s [%(filename)s ] [%(lineno)d] [%(funcName)s] [%(levelname)s]: %(message)s",
                    datefmt="%Y/%m/%d %H:%M:%S",     #日期的格式，可以不写
                    handlers=[
                        logging.StreamHandler(),  #输出到控制台
                        logging.FileHandler(os.path.join(basedir,'log',"log.txt"),encoding= "utf-8")    #输出到文件
                              ]
                    )

#邮件配置
email_config = {
    "server": "smtp.163.com",
    "user" : "xiaqianru@163.com",
    "password": "Xqr63829186",
    "body": "Hi,all.测试报告请看附件",
    "subject": "接口测试报告",
    "receiver": "63829186@qq.com"
}

is_send = False
