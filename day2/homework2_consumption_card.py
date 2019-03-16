import requests


def post_consumption_card():
    url = "http://115.28.108.130:8080/gasStation/process? "
    data = {"dataSourceId": "bG9uZ3Rlbmd0ZXN0", "methodId": "04A", "CardUser": {"userId": "9999"	}, "CardInfo": {"cardNumber": "2019022700", "cardBalance": "10"	}}
    res = requests.post(url=url, json=data)
    print(res.json())


def post_consumption_morethan_cardbalance():
    url = "http://115.28.108.130:8080/gasStation/process? "
    data = {"dataSourceId": "bG9uZ3Rlbmd0ZXN0", "methodId": "04A", "CardUser": {"userId": "9999"	}, "CardInfo": {"cardNumber": "2019022700", "cardBalance": "1000000"	}}
    res = requests.post(url=url, json=data)
    print(res.json())


def post_consumption_error_cardbalace():
    url = "http://115.28.108.130:8080/gasStation/process? "
    data = {"dataSourceId": "bG9uZ3Rlbmd0ZXN0", "methodId": "04A", "CardUser": {"userId": "9999"	}, "CardInfo": {"cardNumber": "2019022700", "cardBalance": "-10"	}}
    res = requests.post(url=url, json=data)
    print(res.json())


def post_consumption_point_cardbalace():
    url = "http://115.28.108.130:8080/gasStation/process? "
    data = {"dataSourceId": "bG9uZ3Rlbmd0ZXN0", "methodId": "04A", "CardUser": {"userId": "9999"	}, "CardInfo": {"cardNumber": "2019022700", "cardBalance": "10.50"	}}
    res = requests.post(url=url, json=data)
    print(res.json())


def post_consumption_special_cardbalace():
    url = "http://115.28.108.130:8080/gasStation/process? "
    data = {"dataSourceId": "bG9uZ3Rlbmd0ZXN0", "methodId": "04A", "CardUser": {"userId": "9999"	}, "CardInfo": {"cardNumber": "2019022700", "cardBalance": "$10"	}}
    res = requests.post(url=url, json=data)
    print(res.json())


def post_consumption_error_cardnumber():
    url = "http://115.28.108.130:8080/gasStation/process? "
    data = {"dataSourceId": "bG9uZ3Rlbmd0ZXN0", "methodId": "04A", "CardUser": {"userId": "9999"	}, "CardInfo": {"cardNumber": "201902270000", "cardBalance": "10"	}}
    res = requests.post(url=url, json=data)
    print(res.json())


def post_consumption_error_user():
    url = "http://115.28.108.130:8080/gasStation/process? "
    data = {"dataSourceId": "bG9uZ3Rlbmd0ZXN0", "methodId": "04A", "CardUser": {"userId": "99990"	}, "CardInfo": {"cardNumber": "2019022700", "cardBalance": "10"	}}
    res = requests.post(url=url, json=data)
    print(res.json())


if __name__ == "__main__":
    # post_consumption_card()
    # post_consumption_morethan_cardbalance()
    # post_consumption_error_cardbalace()
    # post_consumption_point_cardbalace()
    # post_consumption_special_cardbalace()
    # post_consumption_error_cardnumber()
    post_consumption_error_user()