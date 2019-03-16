import logging

# log_level = logging.WARNING  默认为
cmd_handler = logging.StreamHandler()                #输出到屏幕
file_handler = logging.FileHandler("2.log",encoding = "utf-8") #输出到文件


logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s [%(filename)s ] %(lineno)d %(funcName)s %(levelname)s %(message)s",  #大写的DEBUG为10是个常量，小写的事个方法
                    handlers=[cmd_handler,file_handler])                        # 默认输出是GBk格式，是追加模式，  一次运行全局生效

# logger 日志记录器 root 父级log
# handler 日志处理器
# Formatter 日志格式
# Filter 日志过滤器

# 新建一个handler

logging.debug("调试级别的日志")
logging.info("信息级别的日志")
logging.warning("警号级别的日志")
logging.error("错误级别的日志")
logging.critical("严重错误级别的日志")
