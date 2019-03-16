import unittest
import requests


class TestLogin(unittest.TestCase):
    def test_login(self):
        url = "http://115.28.108.130:5000/api/user/login/"
        data = {"name": "张三", "password": "123456"}
        res = requests.post(url=url,data=data)
        print(res.text)
        # res_dict =res.text()
        self.assertEqual("<h1>登录成功</h1>",res.text)
        self.assertIn("登录成功",res.text)


    def test_login_with_wrong(self):
        url = "http://115.28.108.130:5000/api/user/login/"
        data = {"name": "张三1", "password": "1234567"}
        res = requests.get(url=url,data=data)
        print(res.text)
        self.assertIn("失败",res.json())


if __name__ == "__main__":
    pass
