"""用例辅助方法"""
from lib.db import query_db,change_db
import requests


def get_user_data(conn, name):
    result = query_db(conn,"select * from user where name='{}'".format(name))
    return result

def del_user(conn,name):
    result = change_db(conn,"delete  from user where name='{}'".format(name))
    return result


def login(name,password):
    session = requests.session()
    url = "http://115.28.108.130:5000/api/user/login/"
    data = {"name":name, "password":password}
    session.post(url=url,data=data)
    return session
