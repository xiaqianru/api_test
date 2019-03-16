'''项目（全局）配置文件'''
import logging
import time
import os

# 路径配置
# print(os.path.abspath(__file__))   # 当前文件的路径
BASE_DIR = os.path.dirname(os.path.abspath(__file__))    # 当前文件的父路径
DATA_DIR = os.path.join(BASE_DIR,'data')  # 拼接成data数据路径
TEST_DIR = os.path.join(BASE_DIR,'test_case')  # 拼接成test路径
LOG_DIR = os.path.join(BASE_DIR,'log')  # 拼接成log路径
REPORT_DIR = os.path.join(BASE_DIR,'report')  # 拼接成report路径

# 报告配置
REPORT_FILE = os.path.join(REPORT_DIR,"report.html")
REPORT_TITLE = "我的接口测试报告"
REPORT_DESCRIPTION = '''设置接口测试描述
可以有多行
'''

# 日志配置
TODAY = time.strftime("%Y%m%d",time.localtime(time.time()))    #把时间转换成字符串格式
cmd_handler = logging.StreamHandler()                #输出到屏幕
LOG_FILE= os.path.join(LOG_DIR,"{}.log".format(TODAY))
file_handler = logging.FileHandler(LOG_FILE,encoding = "utf-8")   #输出到文件,文件按照当前日期输出
logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s [%(filename)s ] [%(lineno)d] [%(funcName)s] [%(levelname)s]: %(message)s",  #大写的DEBUG为10是个常量，小写的事个方法
                    handlers=[cmd_handler,file_handler])                        # 默认输出是GBk格式，是追加模式，  一次运行全局生效

#数据库配置
DB_CONFIG = {
    "host": "115.28.108.130",
    "port": 3306,
    "user": "test",
    "password": "123456",
    "db": "longtengserver",
    "autocommit": True
}



