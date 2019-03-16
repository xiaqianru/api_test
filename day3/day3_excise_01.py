import requests


def get_tudo_list():
    url = "http://115.28.108.130:5000/todos"
    res = requests.get(url=url)
    print(res.text)



def post_tudo_list():
    url = "http://115.28.108.130:5000/todos"
    data ={"task": "下午三点开会"}
    res = requests.post(url=url, json=data)
    task = res.text.split(":")[1]
    print(task)
    print(res.json()["task"])






if __name__ == "__main__":
    # get_tudo_list()
    post_tudo_list()