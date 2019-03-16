# 1.导入requests
import requests
import json
# 组装


def get_01():
    url = "http://115.28.108.130:5000/add/?a=3&b=5"
    res = requests.get(url=url)
    print(res.text)


def get_02():
    url = "http://115.28.108.130:5000/add/"
    params = {"a": 13, "b": 5}
    res = requests.get(url=url,params=params)
    print(res.text)


def post_form():
    url = "http://115.28.108.130:5000/api/user/login/"
    data = {"name": "张三", "password":"123456"}
    res = requests.post(url=url,data=data)
    print(res.text)  # 响应的字典格式


def post_json_01():
    url = "http://115.28.108.130:5000/api/user/reg/"
    data = {"name": "张三", "password":"123456"}
    res = requests.post(url=url,json=data)
    print(res.json())  # 响应的字典格式
    print(res.json()["msg"])  # 响应的字典格式，响应不是json格式会报错
    print(res.json().get("msg"))  # 响应的字典格式 第二种方式


def post_json_02():
    url = "http://115.28.108.130:5000/api/user/reg/"
    data ='''{
        "name":"张三",
        "password":"123456"
    }
     '''
    headers = {"Content-Type": "application/json"}
    res = requests.post(url=url,data=data.encode('utf-8'),headers=headers)
    print(res.json().get("msg"))  # 响应的字典格式 第二种方式


def post_json_03():
    url = "http://115.28.108.130:5000/api/user/reg/"
    data = {"name": "张三", "password":"123456"}
    headers = {"Content-Type": "application/json"}
    res = requests.post(url=url, data=json.dumps(data), headers=headers)
    # print(res.json().get("msg"))  # 响应的字典格式 第二种方式
    res_dict = res.json()
    print(res.text)
    print(json.dumps(res_dict,indent=2,ensure_ascii=False,sort_keys=True))


def post_xml():
    url = "http://httpbin.org/post"
    data = '''<xml><name>zhangsan</name></xml>
    '''
    headers = {"Content-Type": "application/xml"}
    res = requests.post(url=url,data=data,headers=headers)
    print(res.text)


def post_file():
    url = "http://115.28.108.130:5000/api/user/uploadImage/"
    files = {"file": open("1.txt", "rb"), "img": open("1.jpg")}  # 二进制格式打开
    res = requests.post(url=url,files=files)
    print(res.text)


def get_basic_auth():
    url = "http://115.28.108.130:5000/api/user/login2/"
    res = requests.get(url=url,auth=("admin", "secret"))
    print(res.text)


# 下面要打印出用户信息的内容，有四种方法，
# get_user_list()第一个是分成两部分，取cookies
# get_user_list_1()第二个是用headers里面带cookies方式
# get_user_list_0()第三个是直接用cookies的方式
# get_user_list_2()第四个是用session的方式维持一个会话，不用手工截取cookies
# 二三两个方法都是需要手工截取cookies，第四个方式是最常用方法
def get_user_list():
    url_login = "http://115.28.108.130:5000/api/user/login/"
    data_login = {"name": "张三", "password": "123456"}
    res_login = requests.post(url=url_login, data=data_login)
    print(res_login.text)
    # cookie = res_login.cookies
    url = "http://115.28.108.130:5000/api/user/getUserList/"
    res = requests.get(url=url, cookies=res_login.cookies)
    print(res.text)


def get_user_list_1():  # 使用的是headers方式，所以cookie用的是字符串格式，需要和下面的使用cookies的方式区别
    url = "http://115.28.108.130:5000/api/user/getUserList/"
    headers = {"Cookie":"PYSESSID=8e165a2a-3804-11e9-8a4c-00163e06e52c; session=eyI4ZTE2NWEyYS0zODA0LTExZTktOGE0Yy0wMDE2M2UwNmU1MmMiOnRydWV9.D1PXDg.ZHqMvd12PluQDawjvFdJm4CCy_U"}
    res = requests.get(url=url,headers=headers)
    print(res.text)


def get_user_list_0():   #  使用的是cookies参数，使用的是字典格式，要和上面使用headers方式的字符串格式做区别
    url = "http://115.28.108.130:5000/api/user/getUserList/"
    cookies = {
        "PYSESSID": "8e165a2a-3804-11e9-8a4c-00163e06e52c",
        "session": "eyI4ZTE2NWEyYS0zODA0LTExZTktOGE0Yy0wMDE2M2UwNmU1MmMiOnRydWV9.D1PXDg.ZHqMvd12PluQDawjvFdJm4CCy_U"
         }
    res = requests.get(url=url,cookies=cookies)
    print(res.text)


def get_user_list_2():
    session = requests.session()
    url = "http://115.28.108.130:5000/api/user/login/"
    data = {"name": "张三", "password": "123456"}
    res = session.post(url=url,data=data,)
    url2 = "http://115.28.108.130:5000/api/user/getUserList/"
    res2 = session.get(url=url2)
    print(res2.text)


def login(username,password):
    session = requests.session()
    url = "http://115.28.108.130:5000/api/user/login/"
    data = {"name": username, "password": password}
    res = session.post(url=url,data=data,)
    return session


def get_user_list_3():
    s = login("张三","123456")
    url2 = "http://115.28.108.130:5000/api/user/getUserList/"
    res2 = s.get(url=url2)
    print(res2.text)


def post_update_user():
    s = login("张三","123456")
    url = "http://115.28.108.130:5000/api/user/getToken/?appid=136425"
    res = s.get(url=url)
    token1 = res.text.split("=")[1]
    print(res.text)
    print(token1)
    # url1 = "http://115.28.108.130:5000/api/user/updateUser/?" + res.text
    url1 = "http://115.28.108.130:5000/api/user/updateUser/?token={}" .format(token1)
    print(url1)
    data = {
        "name": "李六",
        "password": "123456"
    }
    res1 = s.post(url=url1,json=data,)
    print(res1.json())
    print(res1.json()["msg"])
    res_dict = res1.json()
    print(json.dumps(res_dict,indent=2,ensure_ascii=False,sort_keys=True))

def get_token():
    url = "http://115.28.108.130:5000/api/user/getToken/?appid=136425"
    res = requests.get(url=url)
    print(res.text)
    token = res.text.split("=")[1]
    return token


def update_user1():
    token = get_token()
    url =  "http://115.28.108.130:5000/api/user/updateUser/?token={}" .format(token)  # 大括号叫占位符，后面占用的填补这个
    print(url)
    res = requests.post(url= url,json={"name": "李六","password": "123456"})
    print(res.json())


def my_format():
    text = {"你好","北京天气","讲个笑话","北京五星酒店"}
    for i in text:
        url = "http://www.tuling123.com/openapi/api?key=ec961279f453459b9248f0aeb6600bbe&info={}".format(i)
        print(url)
        res = requests.get(url=url)
        print(res.text)


def batch_reg():
    users = ["王一", "王二","王三","王四" ]
    url = "http://115.28.108.130:5000/api/user/reg/"
    data = {"name": "张三", "password":"123456"}
    for user in users:
        # data["name"] = user
        data.update( {"name":user,"password":"234567"})
        res = requests.post(url=url,json=data)
        print(res.json())  # 响应的字典格式


if __name__ == "__main__":  # 只有本模块自己运行时才会执行的代码,通常用来调试
    # get_01()
    # get_02()
    # post_form()
    # post_json_01()
    # post_json_02()
    # post_json_03()
    # post_xml()
    # post_file()
    # get_basic_auth()
    # get_user_list()
    # get_user_list_1()
    # get_user_list_2()
    # get_user_list_0()
    # get_user_list_3()
    # post_update_user()
    # update_user1()
    # my_format()
    batch_reg()

