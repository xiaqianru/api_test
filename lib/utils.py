import json
import logging

def json2dict(json_string):   # json转字符串
    if json_string:   # 如果json格式不为空就处理，为空就不处理
        try:
            return json.loads(json_string)
        except json.decoder.JSONDecodeError:
            logging.error("json格式错误：{}".format(json_string))
