# json字符串和字典

# json字符串定义：
# 有大括号{}
# 有冒号：
# 有双引号“”  （json只能用双引号，字典可用单引号，可以用双引号）
# 有对应的值“key”：“张三”/123.00/true/false/null（字典里面True，False，Null）
# 键值中间必须有逗号，最后不能有逗号（和字典一样）
# 不支持备注

# json字符串和字典的区别
# 1.json字符串格式，字典是字典格式
# json只能用“”，字典可以用“”，''
# json中true/false/null,字典中True，False、None
# json不支持备注，字典支持
#
# json字符串和字典的相互转换

import json

# 字典->json字符串
d = {'b': '张三', "a": 1, "d": False, "c": None}
json_str1 = json.dumps(d, ensure_ascii=False)
json_str2 = json.dumps(d, indent=2, ensure_ascii=False, sort_keys=True)
print(json_str1, json_str2)
print(type(d), type(json_str2))
# ensure_ascii=False 不转成asc码，sort_keys=True，按键值排序


# json字符串->字典
# 字符串方便传输，不方便取值
res_text = '{"task": "记得买菜"}'
res_dict= json.loads(res_text)
print(type(res_text),type(res_dict))
print(res_dict["task"])