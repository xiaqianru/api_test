import unittest
import requests


class TestBindingFuelCard(unittest.TestCase):
    def test_binding_fuel_card(self):
        url = "http://115.28.108.130:8080/gasStation/process"
        data ={"dataSourceId":"bHRz","methodId":"01A","CardUser":{"userName":"xiaojuan","idType":"1","idNumber":"110101199808011801","email":"123456@163.com","gender":"1"},"CardInfo":{"cardNumber":"2019030500"}}
        expect = {"code":5010,"msg":"绑定成功","result":{"UserId":6903},"success":True}
        res = requests.post(url = url,json = data)
        self.assertEqual(expect, res.json())


    def test_binding_exist_fuel_card(self):
        url = "http://115.28.108.130:8080/gasStation/process"
        data ={"dataSourceId":"bHRz","methodId":"01A","CardUser":{"userName":"xiaojuan","idType":"1","idNumber":"110101199808011801","email":"123456@163.com","gender":"1"},"CardInfo":{"cardNumber":"1234567890"}}
        expect = {"code":5041,"msg":"卡已经被绑定,无法绑定","success":False}
        res = requests.post(url = url,json = data)
        self.assertEqual(expect, res.json())



if __name__ == '__main__':
    unittest.main()
