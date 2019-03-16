import pymysql
import requests
from homework.homework3_test_data import DB_longtengserver,CardNumber,URL,DataSourceID,MethodId_00A,MethodId_01A,UserID,UserName,IdNumber,IdType
from homework.homework3_test_data import MethodID_03A,CardBalance

def get_conn(DB_longtengserver):
    conn = pymysql.connect(**DB_longtengserver)
    return conn


def select_card_number(conn,cardnumber):
    # conn = get_conn()
    cur = conn.cursor()
    cur.execute("select * from cardinfo where cardnumber = '{}'".format(cardnumber))
    result = cur.fetchall()
    return result


def del_card_number(conn,cardnumber):
    try:
        # conn = get_conn()
        cur = conn.cursor()
        cur.execute("delete  from cardinfo where cardnumber = '{}'".format(cardnumber))
        conn.commit()
    except Exception as ex:
        conn.rollback()


def install_card_number(conn,cardnumber):
    try:
        # conn = get_conn()
        cur = conn.cursor()
        cur.execute("insert into cardinfo set cardnumber = '{}'".format(cardnumber))
        conn.commit()
    except Exception as ex:
        conn.rollback()


def check_card_or_del(conn,cardnumber):
    result = select_card_number(conn,cardnumber)
    if result:
        del_card_number(conn,cardnumber)


def add_new_card(CardNumber):
    data = {"dataSourceId": DataSourceID, "methodId": MethodId_00A, "CardInfo": {"cardNumber": CardNumber}}
    res = requests.post(url=URL, json=data)

def binding_card(CardNumber):
    data = {"dataSourceId": DataSourceID,
            "methodId": MethodId_01A,
            "CardUser":
                {"userName": UserName,
                 "idType": IdType,
                 "idNumber": IdNumber},
            "CardInfo":
                {"cardNumber": CardNumber}
            }
    res = requests.post(url=URL, json=data)


def recharge_card(CardNumber):
    data = {"dataSourceId": DataSourceID, "methodId": MethodID_03A, "CardInfo": {"cardNumber": CardNumber, "cardBalance": CardBalance}}
    res =requests.post(url=URL,json=data)

if __name__ == "__main__":
    conn = get_conn(DB_longtengserver)
    # check_card_number(2019030500)
    # del_card_number(2019030500)
    install_card_number(conn,CardNumber)
    #check_card_or_del(2019030500)




