import requests


def post_add_new_card():
    url = "http://115.28.108.130:8080/gasStation/process"
    data = {"dataSourceId": "c29uZ3Nvbmc=",	"methodId": "00A", "CardInfo": {"cardNumber": "2019022700"}}
    res = requests.post(url=url, json=data)
    print(res.json())


def post_add_old_card():
    url = "http://115.28.108.130:8080/gasStation/process"
    data = {"dataSourceId": "c29uZ3Nvbmc=",	"methodId": "00A", "CardInfo": {"cardNumber": "2019022700"}}
    res = requests.post(url=url, json=data)
    print(res.json())


def post_add_second_card():
    url ="http://115.28.108.130:8080/gasStation/process"
    data ={"dataSourceId": "c29uZ3Nvbmc=",	"methodId": "00A", "CardInfo": {"cardNumber": "2019022701"}}
    res = requests.post(url=url,json=data)
    print(res.json())


def post_add_3th_card():
    url ="http://115.28.108.130:8080/gasStation/process"
    data ={"dataSourceId": "c29uZ3Nvbmc=",	"methodId": "00A", "CardInfo": {"cardNumber": "2019022702"}}
    res = requests.post(url=url,json=data)
    print(res.json())

def post_error_data():
    url ="http://115.28.108.130:8080/gasStation/process"
    data ={"dataSourceId": "c29uZ3Nvbmc=",	"methodId": "00A", "CardInfo": "","cardNumber": "2019022702"}
    res = requests.post(url=url,json=data)
    print(res.json())


def post_error_dataSourceId():
    url ="http://115.28.108.130:8080/gasStation/process"
    data ={"dataSourceId": "c29uZ3Nvbmc",	"methodId": "00A", "CardInfo": {"cardNumber": "2019022702"}}
    res = requests.post(url=url,json=data)
    print(res.json())


def post_error_cardNumber():
    url ="http://115.28.108.130:8080/gasStation/process"
    data ={"dataSourceId": "c29uZ3Nvbmc=",	"methodId": "00A", "CardInfo": {"cardNumber": ""}}
    res = requests.post(url=url,json=data)
    print(res.json())


def post_error_methodId():
    url = "http://115.28.108.130:8080/gasStation/process"
    data = {"dataSourceId": "c29uZ3Nvbmc=",	"methodId": "", "CardInfo": {"cardNumber": "2019022700"}}
    res = requests.post(url=url, json=data)
    print(res.json())



if __name__ == "__main__":
    # post_add_new_card()
    # post_add_old_card()
    # post_add_second_card()
    # post_add_3th_card()
    # post_error_card()
    # post_error_dataSourceId()
    # post_error_cardNumber()
    post_error_methodId()