import requests


def post_recharge_card():
    url = "http://115.28.108.130:8080/gasStation/process? "
    data = {"dataSourceId": "bG9uZ3Rlbmd0ZXN0", "methodId": "03A", "CardInfo": {"cardNumber": "2019022700", "cardBalance": "50"}}
    res = requests.post(url=url,json=data)
    print(res.json())


def post_recharge_null_methodId():
    url = "http://115.28.108.130:8080/gasStation/process? "
    data = {"dataSourceId": "bG9uZ3Rlbmd0ZXN0", "methodId": "", "CardInfo": {"cardNumber": "2019022700", "cardBalance": "50"}}
    res = requests.post(url=url,json=data)
    print(res.json())


def post_recharge_null_dataSourceId():
    url = "http://115.28.108.130:8080/gasStation/process? "
    data = {"dataSourceId": "", "methodId": "03A", "CardInfo": {"cardNumber": "2019022700", "cardBalance": "50"}}
    res = requests.post(url=url,json=data)
    print(res.json())


def post_recharge_null_card():
    url = "http://115.28.108.130:8080/gasStation/process? "
    data = {"dataSourceId": "bG9uZ3Rlbmd0ZXN0", "methodId": "03A", "CardInfo": {"cardNumber": "", "cardBalance": "50"}}
    res = requests.post(url=url,json=data)
    print(res.json())


def post_recharge_null_cardBalance():
    url = "http://115.28.108.130:8080/gasStation/process? "
    data = {"dataSourceId": "bG9uZ3Rlbmd0ZXN0", "methodId": "03A", "CardInfo": {"cardNumber": "2019022700", "cardBalance": ""}}
    res = requests.post(url=url,json=data)
    print(res.json())


def post_recharge_error_methodId():
    url = "http://115.28.108.130:8080/gasStation/process? "
    data = {"dataSourceId": "bG9uZ3Rlbmd0ZXN0", "methodId": "09A", "CardInfo": {"cardNumber": "2019022700", "cardBalance": "50"}}
    res = requests.post(url=url,json=data)
    print(res.json())


def post_recharge_error_dataSourceId():
    url = "http://115.28.108.130:8080/gasStation/process? "
    data = {"dataSourceId": "bG9uZ3Rlbmd0ZXN0==", "methodId": "03A", "CardInfo": {"cardNumber": "2019022700", "cardBalance": "50"}}
    res = requests.post(url=url,json=data)
    print(res.json())


def post_recharge_error_card():
    url = "http://115.28.108.130:8080/gasStation/process? "
    data = {"dataSourceId": "bG9uZ3Rlbmd0ZXN0", "methodId": "03A", "CardInfo": {"cardNumber": "201902270000", "cardBalance": "50"}}
    res = requests.post(url=url,json=data)
    print(res.json())


def post_recharge_error_cardBalance():
    url = "http://115.28.108.130:8080/gasStation/process? "
    data = {"dataSourceId": "bG9uZ3Rlbmd0ZXN0", "methodId": "03A", "CardInfo": {"cardNumber": "2019022700", "cardBalance": "-50"}}
    res = requests.post(url=url,json=data)
    print(res.json())


def post_recharge_black_card():
    url = "http://115.28.108.130:8080/gasStation/process? "
    data = {"dataSourceId": "bG9uZ3Rlbmd0ZXN0", "methodId": "03A", "CardInfo": {"cardNumber": "2019022699", "cardBalance": "50"}}
    res = requests.post(url=url,json=data)
    print(res.json())


def post_recharge_registration_card():
    url = "http://115.28.108.130:8080/gasStation/process? "
    data = {"dataSourceId": "bG9uZ3Rlbmd0ZXN0", "methodId": "03A", "CardInfo": {"cardNumber": "2019022698", "cardBalance": "50"}}
    res = requests.post(url=url,json=data)
    print(res.json())


def post_recharge_company_card():
    url = "http://115.28.108.130:8080/gasStation/process? "
    data = {"dataSourceId": "bG9uZ3Rlbmd0ZXN0", "methodId": "03A", "CardInfo": {"cardNumber": "2019022697", "cardBalance": "50"}}
    res = requests.post(url=url,json=data)
    print(res.json())


if __name__ == "__main__":
    # post_recharge_card()
    # post_recharge_null_methodId()
    # post_recharge_null_dataSourceId()
    # post_recharge_null_card()
    # post_recharge_null_cardBalance()
    # post_recharge_error_methodId()
    # post_recharge_error_dataSourceId()
    # post_recharge_error_card()
    # post_recharge_error_cardBalance()
    # post_recharge_black_card()
    # post_recharge_registration_card()
    post_recharge_company_card()