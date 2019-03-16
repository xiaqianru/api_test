import unittest
import requests
from common import login


class TestLogin(unittest.TestCase):
    def test_login(self):
        url = "http://115.28.108.130:5000/api/user/login/"
        data = {"name": "张三", "password": "123456"}
        session = requests.session()
        s= session.post(url=url,data=data)
        url1= "http://115.28.108.130:5000/api/user/getUserList/"
        res = session.get(url=url1)
        print(res.text)
        self.assertIn("张三",res.text)

    #
    # def test_login_with_wrong(self):
    #     url = "http://115.28.108.130:5000/api/user/login/"
    #     data = {"name": "张三", "password": "1234567"}
    #     res = requests.get(url=url,data=data)
    #     print(res.text)
    #     self.assertIn("登录失败",res.text)
    #

if __name__ == "__main__":
    pass
