import requests


def post_binding_card():
    url = "http://115.28.108.130:8080/gasStation/process"
    data = {"dataSourceId": "c29uZ3Nvbmc=", "methodId": "01A", "CardUser": {"userName": "rainy", "idType": "1", "idNumber": "20190221"}, "CardInfo": {"cardNumber": "2019022700"}}
    res = requests.post(url=url, json=data)
    print(res.json())


def post_repeat_binding_card():
    url = "http://115.28.108.130:8080/gasStation/process"
    data = {"dataSourceId": "c29uZ3Nvbmc=", "methodId": "01A", "CardUser": {"userName": "rainy", "idType": "1", "idNumber": "20190221"}, "CardInfo": {"cardNumber": "2019022700"}}
    res = requests.post(url=url, json=data)
    print(res.json())


def post_binding_second_card():
    url = "http://115.28.108.130:8080/gasStation/process"
    data = {"dataSourceId": "c29uZ3Nvbmc=", "methodId": "01A", "CardUser": {"userName": "rainy", "idType": "1", "idNumber": "20190221"}, "CardInfo": {"cardNumber": "2019022701"}}
    res = requests.post(url=url, json=data)
    print(res.json())


def post_binding_3th_card():
    url = "http://115.28.108.130:8080/gasStation/process"
    data = {"dataSourceId": "c29uZ3Nvbmc=", "methodId": "01A", "CardUser": {"userName": "rainy", "idType": "1", "idNumber": "20190221"}, "CardInfo": {"cardNumber": "2019022702"}}
    res = requests.post(url=url, json=data)
    print(res.json())


def post_binding_error_cardnumber():
    url = "http://115.28.108.130:8080/gasStation/process"
    data = {"dataSourceId": "c29uZ3Nvbmc=", "methodId": "01A", "CardUser": {"userName": "rainy", "idType": "1", "idNumber": "20190221"}, "CardInfo": {"cardNumber": "20190227020"}}
    res = requests.post(url=url, json=data)
    print(res.json())


def post_binding_error_methodId():
    url = "http://115.28.108.130:8080/gasStation/process"
    data = {"dataSourceId": "c29uZ3Nvbmc=", "methodId": "08A", "CardUser": {"userName": "rainy", "idType": "1", "idNumber": "20190221"}, "CardInfo": {"cardNumber": "20190227020"}}
    res = requests.post(url=url, json=data)
    print(res.json())


def post_binding_black_card():
    url = "http://115.28.108.130:8080/gasStation/process"
    data = {"dataSourceId": "c29uZ3Nvbmc=", "methodId": "01A", "CardUser": {"userName": "rainy", "idType": "1", "idNumber": "20190221"}, "CardInfo": {"cardNumber": "2019022699"}}
    res = requests.post(url=url, json=data)
    print(res.json())


def post_binding_registration_card():
    url = "http://115.28.108.130:8080/gasStation/process"
    data = {"dataSourceId": "c29uZ3Nvbmc=", "methodId": "01A", "CardUser": {"userName": "rainy", "idType": "1", "idNumber": "20190221"}, "CardInfo": {"cardNumber": "2019022698"}}
    res = requests.post(url=url, json=data)
    print(res.json())


def post_binding_company_card():
    url = "http://115.28.108.130:8080/gasStation/process"
    data = {"dataSourceId": "c29uZ3Nvbmc=", "methodId": "01A", "CardUser": {"userName": "rainy", "idType": "1", "idNumber": "20190221"}, "CardInfo": {"cardNumber": "2019022697"}}
    res = requests.post(url=url, json=data)
    print(res.json())

if __name__ == "__main__":
    # post_binding_card()
    # post_repeat_binding_card()
    # post_binding_second_card()
    # post_binding_3th_card()
    # post_binding_error_cardnumber()
    # post_binding_error_methodId()
    # post_binding_black_card()
    # post_binding_registration_card()
    post_binding_company_card()