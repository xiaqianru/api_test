#1.导入requests
import requests

#2.组装请求

#3.发送请求并获取响应对象
res = requests.get(url="http://www.baidu.com")
#4.响应解析
# print(res.text)   #获取响应文本
# print(res.status_code,res.reason)
# print(res.content)  #二进制格式
print(res.encoding)  #当前content->text的解码格式
print(res.apparent_encoding)   #真实的解码格式
res.encoding = 'utf-8'  #修改解码格式
print(res.text)
print(res.headers)   #获取响应头（字典格式）
print(res.cookies.get("BDORZ"))  #从响应cookies中获取对应值





