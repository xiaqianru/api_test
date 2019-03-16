import requests


def get_search_card():
    url = "http://115.28.108.130:8080/gasStation/process?"
    params = {"methodId": "02A", "userId": "9999", "cardNumber": "2019022700", "dataSourceId": "bG9uZ3Rlbmd0ZXN0"}
    res = requests.get(url=url, params=params)
    print(res.json())


def get_search_null_card():
    url = "http://115.28.108.130:8080/gasStation/process?"
    params = {"methodId": "02A", "userId": "9999", "cardNumber": "20190227001", "dataSourceId": "bG9uZ3Rlbmd0ZXN0"}
    res = requests.get(url=url, params=params)
    print(res.json())


def get_search_null_user():
    url = "http://115.28.108.130:8080/gasStation/process?"
    params = {"methodId": "02A", "userId": "99990", "cardNumber": "2019022700", "dataSourceId": "bG9uZ3Rlbmd0ZXN0"}
    res = requests.get(url=url, params=params)
    print(res.json())


def get_search_null_dataSourceId():
    url = "http://115.28.108.130:8080/gasStation/process?"
    params = {"methodId": "02A", "userId": "9999", "cardNumber": "2019022700", "dataSourceId": "bG9uZ3Rlbmd0ZXN0="}
    res = requests.get(url=url, params=params)
    print(res.json())


def get_search_blackl_card():
    url = "http://115.28.108.130:8080/gasStation/process?"
    params = {"methodId": "02A", "userId": "9999", "cardNumber": "2019022699", "dataSourceId": "bG9uZ3Rlbmd0ZXN0"}
    res = requests.get(url=url, params=params)
    print(res.json())


def get_search_registration_card():
    url = "http://115.28.108.130:8080/gasStation/process?"
    params = {"methodId": "02A", "userId": "9999", "cardNumber": "2019022698", "dataSourceId": "bG9uZ3Rlbmd0ZXN0"}
    res = requests.get(url=url, params=params)
    print(res.json())


def get_search_company_card():
    url = "http://115.28.108.130:8080/gasStation/process?"
    params = {"methodId": "02A", "userId": "9999", "cardNumber": "2019022697", "dataSourceId": "bG9uZ3Rlbmd0ZXN0"}
    res = requests.get(url=url, params=params)
    print(res.json())


def get_search_recharge_card():
    url = "http://115.28.108.130:8080/gasStation/process?"
    params = {"methodId": "02A", "userId": "9999", "cardNumber": "2019022701", "dataSourceId": "bG9uZ3Rlbmd0ZXN0"}
    res = requests.get(url=url, params=params)
    print(res.json())


def get_search_consumption_card():
    url = "http://115.28.108.130:8080/gasStation/process?"
    params = {"methodId": "02A", "userId": "9999", "cardNumber": "2019022700", "dataSourceId": "bG9uZ3Rlbmd0ZXN0"}
    res = requests.get(url=url, params=params)
    print(res.json())


if __name__ == "__main__":
    # get_search_card()
    # get_search_null_card()
    # get_search_null_user()
    # get_search_null_dataSourceId()
    # get_search_blackl_card()
    # get_search_registration_card()
    # get_search_company_card()
    # get_search_recharge_card()
    get_search_consumption_card()